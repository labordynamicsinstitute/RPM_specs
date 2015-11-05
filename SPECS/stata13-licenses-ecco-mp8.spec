Name: stata13-license-ecco-mp8
License: Commercial
Group: Application/Statistics
Summary: Stata 13 license (10-user 8-core Stata network perpetual license) for ECCO
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 13.0
Release: 0 
Requires: stata13 >= 13.0 
Source0: stata13.lic
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the ECCO Linux stata license. You will need to install it before initializing Stata.

%prep
rm -rf %buildroot
mkdir %buildroot

%build
cd %buildroot
#tar xzvf %{SOURCE0}

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata13
install -m 755 %{SOURCE0} %buildroot/usr/local/stata13/stata.lic

%clean
rm -rf %buildroot

%files
%defattr(755,root,root,0755)
/usr/local/stata13/stata.lic

%changelog
* Mon Sep 23 2013 Lars Vilhuber <lars.vilhuber@cornell.edu> - 13.0-1
- Updated spec file to Stata 13

* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
