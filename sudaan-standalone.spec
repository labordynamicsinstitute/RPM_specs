%define sudaan_package      standalone 
%define install_root        /usr/local/Sudaan_9

Name: sudaan
License: Commercial
Group: Application/Statistics
Summary: Sudaan standalone version from RTI.org 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 9.01 
Release: 1 
Source0: sudaan-standalone.tar 
Source1: sudaan-sas9.tar 
Source2: sudaan-manual.tar 
Source3: sudaan-help.tar 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
SUDAAN is a single program comprising a family of 9 analytic procedures designed to analyze complex data sets. SUDAAN Release 9 is an Essential Addition to Your Software Library and a Useful Complement to SAS and SPSS.

%package sas9
Group: Application/Statistics
Summary: Sudaan SAS-callable version from RTI.org
%description sas9
SUDAAN is a single program comprising a family of 9 analytic procedures designed to analyze complex data sets. SUDAAN Release 9 is an Essential Addition to Your Software Library and a Useful Complement to SAS and SPSS.

This is the SAS-callable version. 

%package manual
Group: Application/Statistics
Summary: Sudaan manual from RTI.org
%description manual
SUDAAN is a single program comprising a family of 9 analytic procedures designed to analyze complex data sets. SUDAAN Release 9 is an Essential Addition to Your Software Library and a Useful Complement to SAS and SPSS.

This is the manual.

%package help
Group: Application/Statistics
Summary: Sudaan help files from RTI.org
%description help
SUDAAN is a single program comprising a family of 9 analytic procedures designed to analyze complex data sets. SUDAAN Release 9 is an Essential Addition to Your Software Library and a Useful Complement to SAS and SPSS.

These are the help files.

%prep

%build

echo "
1. Enter the directory where the SUDAAN program files are
   located. (%{install_root}/Standalone or %{install_root}/SAS9)

2. Execute the sudinit program using the following syntax:

   sudinit p=<22-digit product key> c=<company_name> o=<owner>

Enter your name (<owner>) and company (<company_name>) as they should
appear in the SUDAAN banner, and your 22-digit product key. Note that you
should place the company name and owner name in quotes if they contain
spaces. Spaces should not be included in the product key and letters in the
product key may be entered in upper or lower case.
" > README.Sudaan

# write the profile customizations
echo "PATH=\$PATH:%{install_root}/Standalone
[[ -z \$TMPDIR ]] && SUDWORK=/tmp || SUDWORK=\$TMPDIR
export PATH
export SUDWORK" > sudaan.sh

# write the profile customizations
echo "SUDLIB=%{install_root}/$arg
[[ -z \$TMPDIR ]] && SUDWORK=/tmp || SUDWORK=\$TMPDIR
export SUDLIB
export SUDWORK" > sudaan-sas9.sh


%install

install -d -m 755 %buildroot/%{install_root}
install -d -m 755 %buildroot/etc/profile.d
install -m 755 sudaan.sh %buildroot/etc/profile.d/sudaan.sh
install -m 755 sudaan-sas9.sh %buildroot/etc/profile.d/sudaan-sas9.sh

for arg in Standalone SAS9 Help Manual
do
	install -d -m 755 %buildroot/%{install_root}/$arg
	cd %buildroot/%{install_root}/$arg
	case $arg in
		Standalone)
		   tar xf %{SOURCE0}  
		;;
		SAS9)
		   tar xf %{SOURCE1}  
		;;
		Manual)
		   tar xf %{SOURCE2}  
		;;
		Help)
		   tar xf %{SOURCE3}  
		;;
	esac
done
cd %buildroot
#rm README.Sudaan sudaan*sh

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean

%files
%defattr(755,root,root)
%doc README.Sudaan
%{install_root}/Standalone
/etc/profile.d/sudaan.sh

%files sas9
%defattr(755,root,root)
%doc README.Sudaan
%{install_root}/SAS9
/etc/profile.d/sudaan-sas9.sh

%files manual
%defattr(444,root,root)
%{install_root}/Manual
%files help
%defattr(444,root,root)
%{install_root}/Help
