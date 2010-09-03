Summary: VirtualRDC directories on SSG
Name: vrdc-ssg-directories
Version: 1
Release: 0
License: free
Group: System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Puts the VirtualRDC directories onto the SSG.
#%prep
#%setup -q

#%build

%install
rm -rf $RPM_BUILD_ROOT
# directories 
[[ -d $RPM_BUILD_ROOT/home/ssgprojects/virtualrdc ]] || mkdir -p $RPM_BUILD_ROOT/home/ssgprojects/virtualrdc
for dir in decennial  demographic  economic  mixed  rdcprojects
do
  [[ -d $RPM_BUILD_ROOT/home/ssgprojects/virtualrdc/$dir ]] || mkdir -p $RPM_BUILD_ROOT/home/ssgprojects/virtualrdc/$dir
done
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/home/ssgprojects/virtualrdc/decennial  
/home/ssgprojects/virtualrdc/demographic  
/home/ssgprojects/virtualrdc/economic  
/home/ssgprojects/virtualrdc/mixed  
/home/ssgprojects/virtualrdc/rdcprojects
%doc


%changelog
* Fri Sep  3 2010  <virtualrdc@cornell.edu> - 1.0
- Initial build.

