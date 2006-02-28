#!/usr/bin/perl 
#
# This script builds rpms of all R contrib packages available at CRAN.
# Run it with it's stdout and stderr redirected to a logfile, e.g.
#
#   ./build-R-contrib-rpms.pl 2>&1 | tee R-contrib-build.log
#
# Package descriptions and sources are downloaded automatically from
# a CRAN ftp site (configureable below), spec files are generated on 
# the fly. Interpackage dependencies are recognized automatically. 
# The specfiles include runs of "R CMD check" for all packages. The 
# script installs all successfully generated rpms step by step.
#
# Original author of this script is
# A. Gebhardt <albrecht.gebhardt\@uni-klu.ac.at>
#
#Maintainer is
# D. Steuer <detlef.steuer\@gmx.de>


use Net::FTP;
use Fcntl;
use POSIX;
use File::stat;
# use Data::Dumper;
use IO::Handle;
# unbuffered output:
$|=1;

$ENV{'TMPDIR'} = '/var/tmp';

BEGIN{
  #
  # configurable stuff:

  # local rpm settings:
  $rpmsourcedir = "/usr/src/packages/SOURCES";
  $rpmbuildpath = "/usr/src/packages/BUILD";
  $rpmfilepath  = "/usr/src/packages/RPMS";
  $rpmarch      = "ia64";

  # set R_HOME=$prefix/lib/R:
  # $prefix       = "/usr/local";
  #  /usr because SuSe uses it
	
  $prefix       = "/usr";

  push(@INC, $prefix . "/lib/R/share/perl");
}

# check for installed R:
print "check for R ... ";
unless (!system("rpm -q R-base")) {
  die "R base package not installed!";
  exit 1;
}
print "\n";

use R::Dcf;

# ftp settings:
$cran         = "cran.r-project.org";
$contribpath  = "/pub/R/contrib/main";
# enumerate base libraries:

@baselibs=('base','boot','class','cluster','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','methods','mgcv','nlme','nnet','rkward','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils') ;

# start ftp connection to CRAN:
print "initializing PACKAGES list ...\n";

$ftp = new Net::FTP($cran, Debug => 0, Passive => 1);
unless (defined $ftp) {
  die "can't connect to server $cran";
}
print "connected to $cran ...\n";
unless (defined $ftp->login("anonymous",'autorpmbuilder@')) {
  die "can't login to server as anonymous";
}
print "logged in as anonymous ...\n";
unless (defined $ftp->cwd($contribpath)){
  die "can't cd to $contribpath";
}
print "cd to $contribpath successfull ...\n";

do {
  $packagesfile = tmpnam();
} until sysopen(TMPFH, $packagesfile, O_RDWR | O_CREAT | O_EXCL, 0700);
close(TMPFH);


unless (defined $ftp->get("PACKAGES",$packagesfile)){
  die "can't download PACKAGES file";
}

open(TMPFH, $packagesfile);

# start parsing the PACKAGES file:
while($line=<TMPFH>){
  chomp $line;
  # find all lines starting with "Package:"
  if ($line =~ /^Package:\s*(\S+)\s*/) {
    $package=$1;
    $packages->{$package}{'Package'}=$package;
  }
}
close(TMPFH);
unlink($packagesfile);

# now parse the DESCRIPTION files:
do {
  $descriptionfile = tmpnam();
} until sysopen(TMPFH, $descriptionfile, O_RDWR | O_CREAT | O_EXCL, 0600);
close(TMPFH);

@packagenames=keys %{$packages};
foreach $package (@packagenames){
  print "processing DESCRIPTION for package $package\n";

  unless (defined $ftp->get("Descriptions/".$package.".DESCRIPTION", 
                            $descriptionfile)){
    die "can't download DESCRIPTION file for $package";
  }

  $rdcf = R::Dcf->new($descriptionfile);
  foreach $field ('Version','Description','Author','License','BundleDescription',
                  'Title','Contains','Depends','Package','URL','Date'){
    if (defined($rdcf->{$field})){
      $packages->{$package}{$field} = $rdcf->{$field};
    }
  }
  if (defined($packages->{$package}{'Title'})) {
    $packages->{$package}{'Title'} =~ s/\n/ /g ;
  }
}
$ftp->quit;

@packagenames=keys %{$packages};

# handle interpackage dependencies:
# (assuming no circular dependency)
foreach $package (@packagenames){
  print "get package dependencies for $package\n";
  $packages->{$package}{'dependencies'}=(); 
  if(defined($packages->{$package}{'Depends'})){
    foreach $otherpackage (@packagenames) {
      if($package ne $otherpackage){
        if($packages->{$package}{'Depends'} =~ /$otherpackage/){
          print "$package depends on $otherpackage\n";
          push(@{$packages->{$package}{'dependencies'}}, $otherpackage);
        }
      }
    }
  } 
}
# calculate maximum depth of dependency per package
# (recursively)
sub getdepth {
  my $depth=0;
  foreach $deps (@{$packages->{$_[0]}{'dependencies'}}){
   $d=getdepth($deps)+1; 
   $depth=$d if $d>$depth; 
  }
  return $depth;
}
$maxdepth=0;
foreach $package (@packagenames){
  print "get dependency depth for $package ... ";
  $packages->{$package}{'depdepth'}=getdepth($package);
  print "$packages->{$package}{'depdepth'}\n";
  $maxdepth=$packages->{$package}{'depdepth'} 
    if $packages->{$package}{'depdepth'}>$maxdepth;
}

# now generate the spec files:
# do this in $maxdepth passes, packages with lower
# dependency depth first.
for($pass=0; $pass<=$maxdepth; $pass++){
  print "pass for dependency depth $pass\n";
  foreach $package (@packagenames){
    if($packages->{$package}{'depdepth'}==$pass){
      print "processing package $package\n";
    
      # new ftp connection
      
      $ftp = new Net::FTP($cran, Debug => 0, Passive => 1);
      unless (defined $ftp) {
        die "can't connect to server $cran";
      }
      unless (defined $ftp->login("anonymous",'autorpmbuilder@')) {
        die "can't login to server as anonymous";
      }
      unless (defined $ftp->cwd($contribpath)){
        die "can't cd to $contribpath";
      } 
    
      # prepare some rpm variables:
      @version=split(/-/,$packages->{$package}{'Version'});
      $releaseset=0;
      if (!defined($version[1])){
        $version[1]=0;
        $releaseset=1;
      }
    
      # use only first URL:
      if(!defined($packages->{$package}{'URL'})){
        $url="http://cran.r-project.org/contrib"
      } else {
        if($packages->{$package}{'URL'} =~ /({http:\/\/,ftp:\/\/}{\S}+)/){
          $url=$1;
        } else {
          $url="http://cran.r-project.org/contrib"
        }
      }
      if(!defined(($packages->{$package}{'License'}))){
        $license="unknown";
      } else {
        $license=$packages->{$package}{'License'};
        $license =~ s/\n//g;
      }
    
      # collect dependencies:
      # (R-base is in PreReq, not needed here)
      $requires = "";
      if(defined($packages->{$package}{'Depends'})){
		 # Reorganisation of R-base requires to check
		 # dependecies for the packages in baselibs
		 # Those are included in R-base-*.rpm,
		 # but they have no entry in the rpm database
		 # therefore these are not added to the requires list.

       	 foreach $otherpackage (@packagenames) {
        	  if($package ne $otherpackage){
            		if($packages->{$package}{'Depends'} =~ /$otherpackage/){
	  							$inbase = "FALSE";
									foreach $basepackage (@baselibs){
										if ($otherpackage eq $basepackage) {
											$inbase = "TRUE";
										}
									}
									if ($inbase ne "TRUE") {
              			$requires = $requires . " R-" . $otherpackage;
									}
            		}		
          		}
	  		}
      }
    
      # prepare filenames:
      $sourcefile = $packages->{$package}{'Package'} . "_" . 
        $packages->{$package}{'Version'}  . ".tar.gz";
      $rpmfile = $rpmfilepath . "/" . $rpmarch . "/R-" 
        . $packages->{$package}{'Package'} . "-" . 
        $version[0] . ".R" . $version[1]  . "-1." . $rpmarch . ".rpm";
    
      $ftp->binary();
      $download = $rpmsourcedir . "/" . $sourcefile;
      $checkpath = $rpmbuildpath . "/R-" . $packages->{$package}{'Package'} .
                   "-" . $version[0] . ".R" . $version[1] . "/" .
                   $packages->{$package}{'Package'} . ".Rcheck/";
    
      # rpm already built?
      $downloadstat=stat($download);
      $mustdownload=0;
      if($downloadstat){
        $mtime=$ftp->mdtm($sourcefile);
        unless (defined $mtime){
          # ftp timeout?
          warn "can't get mtime of ftp file $sourcefile";
          $mustdownload=0;
        } else {
          if($downloadstat->mtime < $mtime){
            print "ftp file newer, going to download $sourcefile...\n";
            $mustdownload=1;
          }
          else {
            $size=$ftp->size($sourcefile);
            unless (defined $size){
              # ftp timeout?
              warn "can't get size of ftp file $sourcefile";
              $mustdownload=0;
            } else {
              if($downloadstat->mtime >= $mtime and $downloadstat->size!=$size) {
                print "ftp file differs in size, going to download $sourcefile...\n";
                $mustdownload=1;
              }
            }
            warn "already downloaded!\n";
          }
        }
      } else {
        $mustdownload=1
      }
    
      $generatespec=0;
      if($mustdownload==1) {
        $generatespec=1;
        print "downloading $sourcefile...\n";
        unless (defined $ftp->get($sourcefile, $download)){
          warn "can't download $sourcefile file";
          $generatespec=0;
        }
      } else {
        if(stat($rpmfile)){
          if(stat($download)->mtime > stat($rpmfile)->mtime){
            $generatespec=1;
          } else {
            print "rpm $rpmfile is up to date\n";
          }
        } else {
          $generatespec=1;
        } 
      }
    
      $specfile = "R-" . $packages->{$package}{'Package'} . "-"
        . $packages->{$package}{'Version'} . ".spec";
    
      if(stat($specfile)){
        if(stat($rpmfile)){
          if(stat($specfile)->mtime > stat($rpmfile)->mtime){
            $generatespec=0;
          }
        }
      }
      
      if(defined($packages->{$package}{'Contains'})){
        @subpackages=split(/\s+/,$packages->{$package}{'Contains'});
      }
      
      if($generatespec==1){
        if(stat($specfile)){
          system("mv $specfile $specfile.bak");
          warn "backup of $specfile created!\n";
        }
        sysopen(SPECFH, $specfile , O_RDWR | O_CREAT | O_ECXL, 0644) 
          or die "cannot open spec file";
        print "generating specfile ...\n";
        print SPECFH <<EOT
########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library $packages->{$package}{'Package'}
#
# D. Steuer <detlef.steuer\@gmx.de>
#
%define ver      $version[0]
%define packrel  $version[1]
%define rel      1
%define packname $packages->{$package}{'Package'}
%define prefix   $prefix

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
EOT
;
        if($releaseset==0){
          print SPECFH <<EOT
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
EOT
;
        } else {
          print SPECFH <<EOT
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
EOT
;
        }
        print SPECFH <<EOT
Copyright: $license
URL: $url
Group: Applications/Math
Summary: R package %{packname} - $packages->{$package}{'Title'}
BuildRequires: R-base
PreReq: R-base
EOT
;
        if($packages->{$package}{'depdepth'}>0){
          print SPECFH <<EOT
Requires: $requires
EOT
;
        }
        print SPECFH <<EOT
BuildRoot: /var/tmp/%{packname}-buildroot

EOT
;
        if(!defined($packages->{$package}{'Contains'})){
          print SPECFH <<EOT
%description
R package:
$packages->{$package}{'Description'}
EOT
;
        } else {
          print SPECFH <<EOT
%description
R package bundle:
$packages->{$package}{'BundleDescription'}
EOT
;
        }
        print SPECFH <<EOT

Author(s)
$packages->{$package}{'Author'}

$packages->{$package}{'Date'}

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build
cp %{packname}/DESCRIPTION .

%install
rm -rf \$RPM_BUILD_ROOT
mkdir -p \$RPM_BUILD_ROOT%{prefix}/lib/R/library
%{prefix}/bin/R CMD INSTALL -l \$RPM_BUILD_ROOT%{prefix}/lib/R/library %{packname}
%{prefix}/bin/R CMD check %{packname}
EOT
;
        if(!defined($packages->{$package}{'Contains'})){
          print SPECFH <<EOT
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
EOT
;
        } else {
          foreach $subdir (@subpackages){
            print SPECFH <<EOT
test -d %{packname}/$subdir/src && (cd %{packname}/$subdir/src; rm -f *.o *.so)
EOT
;
          }
        }
        print SPECFH <<EOT


%clean
rm -rf \$RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
EOT
;
        if(!defined($packages->{$package}{'Contains'})){
          print SPECFH <<EOT
%{prefix}/lib/R/library/%{packname}
EOT
;
        } else {
          foreach $subdir (@subpackages){
            print SPECFH <<EOT
%{prefix}/lib/R/library/$subdir
EOT
;
          }
        }
        print SPECFH <<EOT


####### end of spec-file ################################################
EOT
;
    
        close(SPECFH);
      }
    
      $ftp->quit;
    
      if(!stat($rpmfile) && stat($specfile) && stat($download)){
        print "building package $rpmfile ...\n";
        system("rpmbuild -bb --clean --target=$rpmarch $specfile");
        if(!stat($rpmfile)){
          print "build failed for $rpmfile\n";
          print "searching for R CMD check output at $checkpath\n ...";
          if(stat($checkpath)){
            print " found\n";
            if(!defined($packages->{$package}{'Contains'})){
              $checkfile = $checkpath . "/" .
                           $packages->{$package}{'Package'} . "-Ex.Rout";
              open(TMPFH, $checkfile); 
              print "contents of $checkfile:\n";
              while($line=<TMPFH>){
                print $line;
              }
            } else {
              @subpackages=split(/\s+/,$packages->{$package}{'Contains'});
              foreach $subdir (@subpackages){
                $checkfile = $checkpath . "/" . $subdir . "/" .
                             $packages->{$package}{'Package'} . "-Ex.Rout";
                open(TMPFH, $checkfile); 
                print "contents of $checkfile:\n";
                while($line=<TMPFH>){
                  print $line;
                }
                close(TMPFH);
              }
            }
          } else {
            print " not found\n";
          }
        } else {
          # install the new rpm (possibly needed by other
          # package as dependency!)
          system("rpm -Uvh $rpmfile");
        }
      }
    }
  }
}

# print a summary:
foreach $package (@packagenames){
  print "checking for package $package ...";
  @version=split(/-/,$packages->{$package}{'Version'});
  $releaseset=0;
  if (!defined($version[1])){
    $version[1]=0;
    $releaseset=1;
  }
  $rpmfile = $rpmfilepath . "/" . $rpmarch . "/R-" . 
    $packages->{$package}{'Package'} . "-" . 
    $version[0] . ".R" . $version[1]  . "-1." . $rpmarch . ".rpm";
  if(stat($rpmfile)){
    print "exists.\n";
  }
  else {
    print "failed!\n";
  }
}


