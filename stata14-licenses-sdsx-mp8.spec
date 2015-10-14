Name: stata14-license-sdsx-mp8
License: Commercial
Group: Application/Statistics
Summary: Stata 14 license (5-user 8-core Stata network perpetual license) for SDSx
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 14.0
Release: 0 
Requires: stata14 >= 14.0 
Source0: stata14.lic
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the SDSx Linux stata license. You will need to install it before initializing Stata.

%prep
rm -rf %buildroot
mkdir %buildroot

%build
cd %buildroot
#tar xzvf %{SOURCE0}

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata14
install -m 755 %{SOURCE0} %buildroot/usr/local/stata14/stata.lic

%clean
rm -rf %buildroot

%files
%defattr(755,root,root,0755)
/usr/local/stata14/stata.lic

%changelog
* Mon Sep 23 2014 Lars Vilhuber <lars.vilhuber@cornell.edu> - 14.0-1
- Updated spec file to Stata 14

* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
