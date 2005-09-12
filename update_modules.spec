Name: update_modules
License: GPL|BSD
Group: None
Summary: Provide update-modules.dep script 
Packager: Lars Vilhuber <lars.vilhuber@cloutier-vilhuber.net>
Version: 0.0.1 
Release: 0 
Source0: update-modules.dep 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch 

%description
Provide update-modules.dep script from 9.1's aaa_base 

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %buildroot/sbin 
install -m 755 -o root -g root %{SOURCE0} %buildroot/sbin 

%clean
rm -rf %buildroot

%files
/sbin/update-modules.dep 


%changelog -n update_modules_dep 
* Wed Oct  6 2004 root <root@belanger> - 
- Initial build.
* Sat May 08 2004 - leen.meyer@home.nl 
- 0.0.1-0: Initial package 


