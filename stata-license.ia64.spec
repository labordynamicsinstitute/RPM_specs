Name: stata-license-ciser
License: Commercial
Group: Application/Statistics
Summary: Stata 8 license from Stata.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8.2 
Release: 0 
Requires: stata-se >= 8.2
Source0: stata8-ia64.license-ciser.tgz  
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64 

%description
This is CISER's Linux Stata license for the Itanium machine. You will need to install it before initializing Stata.

%prep

%build

%install
cd %buildroot
#install -d m 755 %buildroot/usr/local/stata8
#install -m 755 %{SOURCE0} %buildroot/usr/local/stata8
tar xzvf %{SOURCE0}

%clean

%files
/usr/local/stata8/stata.lic
/usr/local/stata8/perpetual-license-codes
/usr/local/stata8/perpetual-license-codes.stata-se
/usr/local/stata8/stata.msg


%changelog
* Thu Mar 31 2005 vilhuber@lservices
- Modified for IA64
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
