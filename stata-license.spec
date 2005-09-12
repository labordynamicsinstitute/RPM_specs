Name: stata-license-ciser
License: Commercial
Group: Application/Statistics
Summary: Stata 8 license from Stata.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8.2 
Release: 0 
Requires: stata >= 8.2
Source0: stata.lic 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
This is CISER's Linux stata license. You will need to install it before initializing Stata.

%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata8
install -m 755 %{SOURCE0} %buildroot/usr/local/stata8

%clean

%files
/usr/local/stata8/stata.lic

%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
