Name: stata12-license-ssg-mp8
License: Commercial
Group: Application/Statistics
Summary: Stata 12 license (5-user 8-core Stata network perpetual license) for SSG/SDS
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 12.0
Release: 0 
Requires: stata12 >= 12.0 stata12-se stata12-std stata12-mp
Source0: stata12-ssg-licenses.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the SSG and SDS cross-platform Linux stata license. You will need to install it before initializing Stata.

%prep
rm -rf %buildroot
mkdir %buildroot

%build
cd %buildroot
tar xzvf %{SOURCE0}

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata12
install -m 755 stata12-ssg.lic %buildroot/usr/local/stata12/stata.lic
rm *lic

%clean
rm -rf %buildroot

%files
%defattr(755,root,root,0755)
/usr/local/stata12/stata.lic

%changelog
* Thu Sep 8 2011 Lars Vilhuber <lars.vilhuber@cornell.edu> - 12.0-1
- Updated spec file to Stata 12

* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
