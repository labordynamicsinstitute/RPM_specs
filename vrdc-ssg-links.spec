Summary: VirtualRDC links on SSG
Name: vrdc-ssg-links
Version: 1
Release: 0
License: free
Group: System
#Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: vrdc-ssg-directories
%description
Puts the VirtualRDC links onto the SSG.
%prep
#%setup -q
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/home/ssgprojects
#%build

%install
# links
[[ -h $RPM_BUILD_ROOT/ssgprojects ]] || ln -s /home/ssgprojects $RPM_BUILD_ROOT/ssgprojects
for link in decennial  demographic  economic  mixed  rdcprojects
do
 [[ -h $RPM_BUILD_ROOT/$link ]] || ln -s /ssgprojects/virtualrdc/$link $RPM_BUILD_ROOT/$link
done
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/ssgprojects
/decennial  
/demographic  
/economic  
/mixed  
/rdcprojects
%doc


%changelog
* Fri Sep  3 2010  <vilhuber@node-1.localdomain> - ssg-directories
- Initial build.

