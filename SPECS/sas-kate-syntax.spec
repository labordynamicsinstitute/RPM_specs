Name: sas-kate-syntax
License: None
Group: Application/Statistics
Summary: SAS Syntax highlighting for Kate 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.0 
Release: 0 
Requires: kdebase3
Source0: sas.xml 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch 

%description
A syntax file for Kate, can be used with SAS program files.

Author: Ian Schmutte
%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/opt/kde3/share/apps/katepart/syntax/
install -m 755 %{SOURCE0} %buildroot/opt/kde3/share/apps/katepart/syntax/

%clean

%files
%defattr(-, root, root)
/opt/kde3/share/apps/katepart/syntax/sas.xml

%changelog
* Tue Aug 11 2009 virtualrdc@cornell.edu
- Initial RPM
