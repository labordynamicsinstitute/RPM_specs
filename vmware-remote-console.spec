Name: VMware-remote-console
License: Commercial
Group: Application
Summary: VMware Server Beta 2 console extracted from XPI
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.0
Release: rc2
Source0: vmware-remote-console.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
VMware Server Beta 2 console extracted from XPI. 

You need to go onto the server and find the xpi for your architecture. Then extract the xpi, go to the plugins directory, that becomes our SOURCE0.

%prep

%build

%install
mkdir -p -m 755 %buildroot/usr/local/bin
cd %buildroot/usr/local/
tar xzvf %{SOURCE0}  
cd bin
echo "#!/bin/bash
/usr/local/vmware-remote-console/vmware-vmrc $*
" > vmware-remote-console
chmod a+rx vmware-remote-console

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/vmware-remote-console
fi

%clean


%files
/usr/local/bin/vmware-remote-console
/usr/local/vmware-remote-console
