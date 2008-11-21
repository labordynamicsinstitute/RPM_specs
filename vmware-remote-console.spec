Name: VMware-remote-console
License: Commercial
Group: Application
Summary: VMware Server Beta 2 console extracted from XPI
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.0
Release: rc2
Source0: vmware-vmrc-linux-x64.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
VMware Server Beta 2 console extracted from XPI. 

You need to go onto the server and find the xpi for your architecture.

%prep

%build
unzip %{SOURCE0}

%install
mkdir -p -m 755 %buildroot/usr/local/bin
mv plugins %buildroot/usr/local/vmware-remote-console
cd %buildroot/usr/local/bin
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


%changelog

* Thu Sep  4 2008 Lars Vilhuber <lars.vilhuber@cornell.edu> - 2.0-rc2
- Modified it to use the XPI directly

%files
/usr/local/bin/vmware-remote-console
/usr/local/vmware-remote-console
