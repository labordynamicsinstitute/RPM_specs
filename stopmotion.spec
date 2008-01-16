# norootforbuild

%define _prefix	/usr

Name:				stopmotion
Version:			0.6.0
Release:			1.suse%(echo "%{suse_version}" | %__sed -e 's/.$//')
Summary:			Application for creating stop-motion animation movies
Source:			http://developer.skolelinux.no/info/studentgrupper/2005-hig-stopmotion/project_management/webpage/releases/stopmotion-%{version}.tar.gz
URL:				http://stopmotion.bjoernen.com/
Group:			Applications/Media
License:			GNU General Public License (GPL)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc-c++ libstdc++ libstdc++-devel zlib zlib-devel
BuildRequires:	libvorbis libvorbis-devel make SDL_image-devel SDL-devel
BuildRequires:	libqt4 libqt4-devel >= 4.2.0 libxml2-devel fam-devel


%description
Stopmotion is a free application for creating stop-motion animation movies. The users will be able to create stop-motions from pictures imported from a camera or from the harddrive, add sound effects and export the animation to different video formats such as mpeg or avi. 

%prep
%setup -q

%build
./configure --prefix=%{buildroot}%{_prefix}
%__make

%install
%__make  install
%__install -D -m0644 stopmotion.1.gz "%{buildroot}%{_mandir}/man1/stopmotion.1.gz"
#%suse_update_desktop_file -r "%{name}" Education Astronomy

%clean
%__rm -rf "%{buildroot}"

%files -f "%{name}.lang"
%defattr(-,root,root)
%{_bindir}/stopmotion
%doc %{_mandir}/man1/stellarium.1*
%doc /usr/share/stopmotion/


%changelog
* Thu Jun 14 2007 Pascal Bleser <guru@unixtech.be> 0.9.0-1
- new upstream version
- now requires qt4 >= 4.2.0, only built on 10.2
- build system changed to cmake

* Tue Aug  8 2006 Pascal Bleser <guru@unixtech.be> 0.8.1-1
- dropped extra qualifier patch, fixed upstream
- new upstream version

* Tue May  2 2006 Pascal Bleser <guru@unixtech.be> 0.8.0-1
- new upstream version

* Sun Apr 23 2006 Pascal Bleser <guru@unixtech.be> 0.7.1-3
- added patch to remove extra qualifiers, fixes build on 10.1

* Sun Apr 23 2006 Pascal Bleser <guru@unixtech.be> 0.7.1-2
- rewrote spec file

* Tue Oct 25 2005 Pascal Bleser <guru@unixtech.be> 0.7.1-1
- new package

# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
