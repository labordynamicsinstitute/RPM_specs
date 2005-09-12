Name: bootsplash-theme-SuSE92 
License: GPL
Group: System/Boot
Summary: SuSE 9.2 Bootsplash Themes
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 3.0 
Release: 0 
Source: bootsplash-SuSE92.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch 

%description
This package contains all bootsplash themes for SuSE 9.2
%prep

%build

%install
cd %buildroot
tar xzvf %{SOURCE0}  

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
#rm -rf %buildroot/usr/local/stata8

%files
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-800x600.cfg
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-1024x768.cfg
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-1600x1200.cfg
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-640x480.cfg
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-1280x1024.cfg
/etc/bootsplash/themes/SuSE-Home/config/bootsplash-1400x1050.cfg
/etc/bootsplash/themes/SuSE-Home/images/silent-1400x1050_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-800x600.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-800x600_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-800x600.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1024x768_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-1024x768.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1600x1200.jpg
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-1600x1200.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1280x1024_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-640x480.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1280x1024.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-640x480.jpg
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-1280x1024.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1400x1050_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-1024x768_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-640x480_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/circclose.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-1600x1200_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-1280x1024_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-800x600_left.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-1600x1200_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/silent-1400x1050.jpg
/etc/bootsplash/themes/SuSE-Home/images/bootsplash-1400x1050.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-1024x768.jpg
/etc/bootsplash/themes/SuSE-Home/images/silent-640x480_right.pbm
/etc/bootsplash/themes/SuSE-Home/images/circopen.pbm
/etc/bootsplash/themes/SuSE-Home/bootloader/message
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.bg
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.de
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.cs
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.el
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.en
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.es
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.fr
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.hu
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.ja
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.it
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.nb
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.nl
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.pl
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.ro
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.ru
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.sk
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.sl
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.sv
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.pt_BR
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.zh_CN
/etc/bootsplash/themes/SuSE-Home/bootloader/texts.zh_TW
/etc/bootsplash/themes/SuSE-Home/bootloader/help.bg
/etc/bootsplash/themes/SuSE-Home/bootloader/help.de
/etc/bootsplash/themes/SuSE-Home/bootloader/help.cs
/etc/bootsplash/themes/SuSE-Home/bootloader/help.en
/etc/bootsplash/themes/SuSE-Home/bootloader/help.es
/etc/bootsplash/themes/SuSE-Home/bootloader/help.fr
/etc/bootsplash/themes/SuSE-Home/bootloader/help.hu
/etc/bootsplash/themes/SuSE-Home/bootloader/help.ja
/etc/bootsplash/themes/SuSE-Home/bootloader/help.it
/etc/bootsplash/themes/SuSE-Home/bootloader/help.nb
/etc/bootsplash/themes/SuSE-Home/bootloader/help.nl
/etc/bootsplash/themes/SuSE-Home/bootloader/help.ro
/etc/bootsplash/themes/SuSE-Home/bootloader/help.sk
/etc/bootsplash/themes/SuSE-9.2/animations/text.mng
/etc/bootsplash/themes/SuSE-9.2/animations/circ.mng
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-800x600.cfg
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-1024x768.cfg
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-1600x1200.cfg
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-640x480.cfg
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-1280x1024.cfg
/etc/bootsplash/themes/SuSE-9.2/config/bootsplash-1400x1050.cfg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-800x600.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-800x600.jpg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-1024x768.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-1600x1200.jpg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-1600x1200.jpg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-640x480.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-1280x1024.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-640x480.jpg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-1280x1024.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-1400x1050.jpg
/etc/bootsplash/themes/SuSE-9.2/images/bootsplash-1400x1050.jpg
/etc/bootsplash/themes/SuSE-9.2/images/silent-1024x768.jpg
/etc/bootsplash/themes/SuSE-9.2/bootloader/message
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.bg
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.de
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.cs
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.el
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.en
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.es
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.fr
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.hu
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.ja
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.it
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.nb
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.nl
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.pl
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.ro
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.ru
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.sk
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.sl
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.sv
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.pt_BR
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.zh_CN
/etc/bootsplash/themes/SuSE-9.2/bootloader/texts.zh_TW
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.bg
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.de
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.cs
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.en
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.es
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.fr
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.hu
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.ja
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.it
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.nb
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.nl
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.ro
/etc/bootsplash/themes/SuSE-9.2/bootloader/help.sk
