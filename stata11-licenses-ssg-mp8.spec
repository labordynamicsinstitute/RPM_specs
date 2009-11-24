Name: stata11-license-ssg-mp8
License: Commercial
Group: Application/Statistics
Summary: Stata 11 license (5-user 8-core Stata network perpetual license) for SSG
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 11.0
Release: 0 
Requires: stata11 >= 11.0 stata11-se stata11-std stata11-mp
Source0: stata11-ssg-mp8.lic 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the SSG cross-platform Linux stata license. You will need to install it before initializing Stata.

%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata11
install -m 755 %{SOURCE0} %buildroot/usr/local/stata11/stata.lic

%clean

%files
%defattr(755,root,root,0755)
/usr/local/stata11/stata.lic

%changelog
* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 11.0-1
- Updated spec file to Stata 11

* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
