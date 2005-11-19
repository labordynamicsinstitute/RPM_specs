# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id: CastPodder.spec,v 1.6 2005/11/19 08:45:38 grayban Exp $

%define		name CastPodder
%define		version 3.2
%define         distribution suse
%define		release 1.0_%{distribution}
%define		__libtoolize /bin/true
%define		__cputoolize /bin/true
%define         packager Lars Vilhuber

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        CastPodder is a Media Aggregator
Packager:       %{packager}
Distribution:   %{distribution}
License:        GPL
URL:            http://borgforge.net/projects/castpodder/
Group:          Sound
Source:         %{name}-%{version}.tar.bz2
Source10:       %{name}-16.png
Source11:       %{name}-32.png
Source12:       %{name}-48.png
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildArch:      noarch
Requires:       python-wxGTK
Requires:       python python-xmms libxml2-python
Obsoletes:	iPodder

%description
CastPodder is technically a "Media Aggregator,"
a program that allows you to select and download audio
files from anywhere on the Internet to your desktop.

CastPodder makes the process easy by helping you select audio files
from among the thousands of audio sources on the web and downloading
those files to your computer. Once you select a feed or location,
it will download those files automatically at times you specify
and have the files waiting for you on your computer,
so you don't have to spend a lot of time manually selecting and waiting
for downloads. You can play your selected audio files using iTunes
or other "jukebox" software, or load them on to your iPod or other
portable digital media player to play anytime you want.

%prep
rm -rf %buildroot

%setup -q -n castpodder
%build



%install

# remove all CVS files so that they don't get "accidently" installed
for CVSDIR in `find . -type d -name CVS` ; do
    /bin/rm -rf $CVSDIR
done

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%{name}
mkdir -p %buildroot/opt/%{name}
cp -f -R * %buildroot/opt/%{name}
cp -f %buildroot/opt/%{name}/%{name}.sh $RPM_BUILD_ROOT/%_bindir/%{name}
chmod -R 755 %buildroot/opt/%{name}/*.py

#menus
#install -d %buildroot/%{_menudir}
#cat <<EOF >%buildroot/%{_menudir}/%{name}
#?package(%{name}):command="%{_bindir}/%{name}" \
#                  icon=%{name}.png \
#                  needs="x11" \
#                  section="Multimedia/Sound" \
#                  title="CastPodder"\
#                  longtitle="%{summary}"
#EOF
#
#install -m644 %{SOURCE10} -D %buildroot/%{_miconsdir}/%{name}.png
#install -m644 %{SOURCE11} -D %buildroot/%{_iconsdir}/%{name}.png
#install -m644 %{SOURCE12} -D %buildroot/%{_liconsdir}/%{name}.png

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README NOTES LICENSE ChangeLog TODO KNOWN-ISSUES docs
%attr(0755,root,root) %{_bindir}/%{name}
/opt/%{name}/*

%pre
# lets make sure nothing is there so we delete the old
# directory first before installing - sgrayban
rm -fr /opt/%{name}

%post
%{update_menus}

%postun
%{clean_menus}


%changelog

* Sat Nov 19 2005 Scott Grayban <sgrayban@castpodder.net> 3.2
 - New version release from the CastPodder Team

* Sat Nov 12 2005 Scott Grayban <sgrayban@castpodder.net> 3.1
 - New version release from the CastPodder Team

* Fri Oct 7 2005 Scott Grayban <sgrayban@borgnet.us> 3.0
 - New version release from the CastPodder Team
