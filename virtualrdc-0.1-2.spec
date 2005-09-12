Summary: Configures a VirtualRDC from scratch or updates an existing one. 
Name: virtualrdc 
Version: 0.1
Release: 1
Copyright: GPL
Group: System Environment/Base
Source: virtualrdc-0.1-2.tar.gz 


%description
* Nondestructively creates RDC directory structure  
* Adds VirtualRDC-specific menus to the KDE/SuSE menu tree
* Removes irrelevant menus and desktop shortcuts 
* Makes VNC-related modifications

%prep 
%setup -c 

%build
echo "!!! virtualrcd build"

%install
echo "!!! virtualrcd install"
#echo "pwd -->" `pwd`

%clean
echo "!!! cleaning script"
rm -rf $RPM_BUILD_ROOT/*



%pre 
echo "!!! pre-install script"
mv /usr/X11R6/bin/vncserver /usr/X11R6/bin/vncserver.pre-%{name}-%{version}
# Creation of SuSE default desktop shortcuts are hardcoded in /opt/kde3/bin/startkde.theme 
# Corresponding .desktop files reside in /opt/kde3/share/config/SuSE/default
# They are renamed to prevent them from being added to desktops of the new users: 
SHORTCUT_DIR="/opt/kde3/share/config/SuSE/default"
for SHORTCUT in "myComputer" "Novell" "SuSE" "YaST" "Network" "Printer"; do
  mv "$SHORTCUT_DIR/$SHORTCUT".desktop "$SHORTCUT_DIR/$SHORTCUT".desktop.VirtualRDC 
done
# Autostart:
# /opt/kde3/share/autostart/susewatcher.desktop

%post 
echo "!!! post-install script" 
ln -s /etc/VirtualRDC/.vnc/xstartup /etc/skel/.vnc/xstartup
ln -s /usr/X11R6/bin/vncserver.wrapper /usr/X11R6/bin/vncserver 
ln -s /usr/X11R6/bin/vncserver.pre-%{name}-%{version} /usr/X11R6/bin/vncserver.local

ln -s /opt/SAS_9.1/sas /usr/local/bin/sas913
ln -s /usr/local/bin/sas913 /usr/local/bin/sas91
ln -s /usr/local/bin/sas91 /usr/local/bin/sas9
ln -s /usr/local/bin/sas9 /usr/local/bin/sas

/etc/VirtualRDC/rdcdirtree/mkrdcdirtree /mirror/rdcserver /etc/VirtualRDC/rdcdirtree

%preun
echo "!!! pre-uninstall script"
rm /etc/skel/.vnc/xstartup
rm /usr/X11R6/bin/vncserver
rm /usr/X11R6/bin/vncserver.local

rm /usr/local/bin/sas
rm /usr/local/bin/sas9
rm /usr/local/bin/sas91
rm /usr/local/bin/sas913

/etc/VirtualRDC/rdcdirtree/rmrdcdirtree /mirror/rdcserver

%postun
echo "!!! post-uninstall script"
#rm -rf /etc/VirtualRDC
SHORTCUT_DIR="/opt/kde3/share/config/SuSE/default"
for SHORTCUT in "myComputer" "Novell" "SuSE" "YaST" "Network" "Printer"; do
  mv "$SHORTCUT_DIR/$SHORTCUT".desktop.VirtualRDC "$SHORTCUT_DIR/$SHORTCUT".desktop
done
mv /usr/X11R6/bin/vncserver.pre-%{name}-%{version} /usr/X11R6/bin/vncserver


%files
/etc/VirtualRDC
/etc/skel/.vnc
/usr/X11R6/bin/listvncs
/usr/X11R6/bin/listmyvncs
/usr/X11R6/bin/vncserver.wrapper
/usr/share/desktop-directories/VirtualRDC.directory
/etc/xdg/menus/applications-merged/VirtualRDC.menu
/opt/kde3/share/applications/kde/VirtualRDC
/etc/VirtualRDC/rdcdirtree

%changelog
* Mon Feb 14 2005 Andrey Balyakin <aab24@cornell.edu>
- KDE menus/shortcuts alteration was included
* Tue Feb 01 2005 Andrey Balyakin <aab24@cornell.edu>
- VNC-related changes were added
* Mon Jan 03 2005 Andrey Balyakin <aab24@cornell.edu> 
- .spec file skeleton is created and RDC directory structure is included
