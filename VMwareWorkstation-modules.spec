%define krelease 2.6.11.4-21.11-default
Name: VMwareWorkstation-Modules
License: Commercial
Group: System
Summary: VMware modules
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 5.5.1 
Release: 2.6.11 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
VMware modules recompiled. This will also set VMware to 'configured'.

%prep

%build

%install
cd %buildroot
install -d -m 755 -o root -g root %buildroot/lib/modules/%{krelease}/misc/
cp -a /lib/modules/%{krelease}/misc/vm* %buildroot/lib/modules/%{krelease}/misc/

%post
test -f /etc/vmware/not_configured && rm -rf /etc/vmware/not_configured
/etc/init.d/vmware start

%postun
/etc/init.d/vmware stop
touch /etc/vmware/not_configured
%clean

%files
/lib/modules/%{krelease}/misc/vmmon.ko
/lib/modules/%{krelease}/misc/vmnet.ko
/lib/modules/%{krelease}/misc/vmmon.o
/lib/modules/%{krelease}/misc/vmnet.o


%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
