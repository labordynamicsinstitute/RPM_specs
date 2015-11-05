%define updatever 20121022
# maintenance of stata:
# on an installed system, run 'update all'
# then tar czf /usr/src/redhat/SOURCES/stata12-linux-$updatevar.tgz /usr/local/stata12

Name: stata12
License: Commercial
Group: Application/Statistics
Summary: Stata 12 (standard) from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 12.0 
Release: %{updatever} 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: stata12-linux-%{updatever}.tgz 
Source1: stata12-desktop.tgz

%description
Installs Stata 12 base files. You will need one of -std, -se, and/or -mp,
depending on your license.

You still need to install the license. You can install the license (as root) by 

cd /usr/local/stata12
./stinit

%package std
Group: Application/Statistics
Summary: Standard version of Stata 
Requires: stata12 >= 12.0
%description std
Standard binaries for Stata.

%package se
Group: Application/Statistics
Summary: SE version of Stata 
Requires: stata12 >= 12.0
%description se
SE binaries for Stata.

%package mp
Group: Application/Statistics
Summary: MP version of Stata 
Requires: stata12 >= 12.0
%description mp
MP binaries for Stata.

%package sm
Group: Application/Statistics
Summary: Small version of Stata 
Requires: stata12 >= 12.0
%description sm
Small Stata binaries.

%package desktop
Group: Application/Statistics
Summary: Desktop integration for Stata 
Requires: stata12 >= 12.0
%description desktop
Creates links and desktop icons for Stata 12

%package mkdefault
Group: Application/Statistics
Summary: Make Stata 12 the default
Requires: stata12 >= 12.0

%description mkdefault
Creates links for Stata 12

%package libgtksourceview
Group: Application/Statistics
Summary: Utility package to provide a fake link on openSUSE for a required library
Requires: stata12 >= 12.0 libgtksourceview-2_0-0
Provides: libgtksourceview-1.0.so.0()(64-bit)

%description libgtksourceview
Utility package to provide a fake link on openSUSE for a required library, which is required for 
Stata 12 to run.

%prep

%build
# make a note for the libgtksourceview package
echo "For openSUSE and other newer distributions, Stata12 needs libgtksourceview.1 libraries.
This were created as links to the version 2 libraries." > README.opensuse

%install
# install the desktop files
tar xzf %{SOURCE1}
# install the desktop stuff 
install -d %buildroot/usr/share/applications
install Stata12.desktop %buildroot/usr/share/applications
install Stata12-SE.desktop %buildroot/usr/share/applications
install Stata12-MP.desktop %buildroot/usr/share/applications

# install the core files
cd %buildroot
install -d %buildroot/usr/local/bin
tar xzvf %{SOURCE0}  
[[ -f usr/local/stata12/stata.lic ]] && \rm -f usr/local/stata12/stata.lic
ln -sf ../stata12/stata %buildroot/usr/local/bin/stata12
ln -sf ../stata12/xstata %buildroot/usr/local/bin/xstata12
ln -sf ../stata12/stata-se %buildroot/usr/local/bin/stata12-se
ln -sf ../stata12/xstata-se %buildroot/usr/local/bin/xstata12-se
ln -sf ../stata12/stata-mp %buildroot/usr/local/bin/stata12-mp
ln -sf ../stata12/xstata-mp %buildroot/usr/local/bin/xstata12-mp
ln -sf ../stata12/stata-sm %buildroot/usr/local/bin/stata12-sm
ln -sf ../stata12/xstata-sm %buildroot/usr/local/bin/xstata12-sm

# install the default stuff 
cd %buildroot/usr/local/bin
ln -sf stata12 stata
ln -sf stata12-se stata-se
ln -sf stata12-mp stata-mp
ln -sf stata12-sm stata-sm
ln -sf xstata12 xstata
ln -sf xstata12-se xstata-se
ln -sf xstata12-mp xstata-mp
ln -sf xstata12-sm xstata-sm

# install the workaround
install -d %buildroot/usr/lib64
touch %buildroot/usr/lib64/libgtksourceview-2.0.so.0
ln -s libgtksourceview-2.0.so.0 %buildroot/usr/lib64/libgtksourceview-1.0.so.0
rm %buildroot/usr/lib64/libgtksourceview-2.0.so.0

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata12
fi

%clean
#rm -rf %buildroot/usr/local/stata12

%changelog
* Mon Dec  7 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 12.0-2
- Moved desktop files to compliant /usr/share/applications location


* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.0-1
- Updated spec file to Stata 12

%files
%defattr(0755,root,root,0755)
/usr/local/stata12/ado/
/usr/local/stata12/docs/
/usr/local/stata12/auto.dta
/usr/local/stata12/isstata.120
/usr/local/stata12/installed.120
/usr/local/stata12/stinit
/usr/local/stata12/stata_br
/usr/local/stata12/stata_pdf
%attr(770,root,root) /usr/local/stata12/inst2
%attr(770,root,root) /usr/local/stata12/setrwxp

%config
/usr/local/stata12/stata.msg
/usr/local/stata12/profile.do

%files libgtksourceview
/usr/lib64/libgtksourceview-1.0.so.0
%doc README.opensuse

%files std
%defattr(0755,root,root,0755)
/usr/local/bin/stata12
/usr/local/bin/xstata12
/usr/local/stata12/stata
/usr/local/stata12/xstata

%files se
%defattr(0755,root,root,0755)
/usr/local/bin/stata12-se
/usr/local/bin/xstata12-se
/usr/local/stata12/stata-se
/usr/local/stata12/xstata-se

%files sm
%defattr(0755,root,root,0755)
/usr/local/bin/stata12-sm
/usr/local/bin/xstata12-sm
/usr/local/stata12/stata-sm
/usr/local/stata12/xstata-sm

%files mp
%defattr(0755,root,root,0755)
/usr/local/stata12/stata-mp
/usr/local/stata12/xstata-mp
/usr/local/bin/stata12-mp
/usr/local/bin/xstata12-mp

%files desktop
%defattr(0755,root,root,0755)
/usr/share/applications/Stata12.desktop
/usr/share/applications/Stata12-MP.desktop
/usr/share/applications/Stata12-SE.desktop
/usr/local/stata12/stata12.png

%files mkdefault
%defattr(755,root,root)
/usr/local/bin/stata
/usr/local/bin/stata-se
/usr/local/bin/stata-mp
/usr/local/bin/stata-sm
/usr/local/bin/xstata
/usr/local/bin/xstata-se
/usr/local/bin/xstata-sm
/usr/local/bin/xstata-mp

