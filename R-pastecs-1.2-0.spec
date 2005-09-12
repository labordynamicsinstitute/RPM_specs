########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library pastecs
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.2
%define packrel  0
%define rel      1
%define packname pastecs
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GNU Public Licence 2.0 or above at your convenience
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Package for Analysis of Space-Time Ecological Series
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Regulation, decomposition and analysis of space-time series. The pastecs library is a PNEC-Art4 and IFREMER (Benoit Beliaeff <Benoit.Beliaeff@ifremer.fr>) initiative to bring PASSTEC 2000 (http://www.obs-vlfr.fr/~enseigne/anado/passtec/passtec.htm) functionnalities to R.

Author(s)
Frederic Ibanez <ibanez@obs-vlfr.fr>, Philippe Grosjean <phgrosjean@sciviews.org> & Michele Etienne <etienne@obs-vlfr.fr>

2004-09-03

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build
cp %{packname}/DESCRIPTION .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/R/library
%{prefix}/bin/R CMD INSTALL -l $RPM_BUILD_ROOT%{prefix}/lib/R/library %{packname}
%{prefix}/bin/R CMD check %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
%{prefix}/lib/R/library/%{packname}


####### end of spec-file ################################################
