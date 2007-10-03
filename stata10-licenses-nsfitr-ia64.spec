Name: stata10-license-nsfitr-ia64
License: Commercial
Group: Application/Statistics
Summary: Stata 10 license (single user, ia64, SE, 10-user) from Stata.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 10.0
Release: 0 
Requires: stata10 >= 10.0 
Source0: stata10-ia64-nsfitr.lic 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64 

%description
This is the NSF-ITR Linux stata license. You will need to install it before initializing Stata.

%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/stata10
install -m 755 %{SOURCE0} %buildroot/usr/local/stata10/stata.lic

%clean

%files
%defattr(755,root,root,0755)
/usr/local/stata10/stata.lic

%changelog
* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 10.0-1
- Updated spec file to Stata 10

* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
