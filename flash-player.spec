Name: flash-plugin-alpha
License: Commercial
Group: Applications/Internet
Summary: Adobe Flash Player 10.0 alpha refresh
Packager: Lars Vilhuber
Vendor: Adobe Systems Inc.
Version: 10.0.32.18
Release: 1
URL: http://labs.adobe.com/downloads/flashplayer10.html
BuildArch: x86_64
Source0: libflashplayer-%{version}.linux-x86_64.so.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 


%description
64-bit Adobe Flash Player 10 for Linux operating systems was released on 12/16/2008. 


%prep

%build

%install
tar xzf %{SOURCE0}
# install the desktop stuff 
install -d %buildroot/usr/lib64/browser-plugins/
install libflashplayer.so %buildroot/usr/lib64/browser-plugins/

%post

%pre
# uninstall the x86 version if installed in the plugin library
if [[ -f /usr/lib64/browser-plugins/npwrapper.libflashplayer.so ]]
then
/usr/bin/nspluginwrapper -r /usr/lib64/browser-plugins/npwrapper.libflashplayer.so
fi

%preun

%postun
# re-install the x86 version if installed in the plugin library
if [[ -f /usr/lib/browser-plugins/libflashplayer.so ]]
then
/usr/bin/nspluginwrapper -i /usr/lib/browser-plugins/libflashplayer.so
fi
%clean

%files
%defattr(755,root,root)
/usr/lib64/browser-plugins/libflashplayer.so

%changelog
* Thu Dec 18 2008 Lars Vilhuber <lars.vilhuber@cornell.edu> - 10.0.d21.1-1
- Initial version

