# norootforbuild

%define _prefix	/usr

Name:				stellarium
Version:			0.9.0
Release:			1.guru.suse%(echo "%{suse_version}" | %__sed -e 's/.$//')
Summary:			Stellarium renders realistic Skies in Real Time with OpenGL
Source:			http://prdownloads.sourceforge.net/stellarium/stellarium-%{version}.tar.gz
Source1:			stellarium.desktop
Source2:			stellarium.png
URL:				http://www.stellarium.org
Group:			Productivity/Scientific/Astronomy
License:			GNU General Public License (GPL)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc-c++ libstdc++ libstdc++-devel zlib zlib-devel curl curl-devel
BuildRequires:	libogg libogg-devel libvorbis libvorbis-devel make
BuildRequires:	Mesa-devel libqt4 libqt4-devel >= 4.2.0
BuildRequires:	cmake >= 2.4.6
BuildRequires:	update-desktop-files
Requires:		dejavu

%description
Stellarium is free GPL software which renders realistic skies in real time
with openGL. It is available for Linux/Unix, Windows and MacOSX.
With Stellarium, you really see what you can see with your eyes, binoculars or
a small telescope. Stellarium is also used in planetariums.

%if %suse_version < 1030
Building this package requires a newer cmake from
http://software.opensuse.org/download/devel:/tools:/building/
%endif

%if %suse_version >= 930
%debug_package
%endif
%prep
%setup -q

%build
cmake -D CMAKE_INSTALL_PREFIX:PATH="%{_prefix}" .
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
%__install -D -m0644 data/stellarium.1 "%{buildroot}%{_mandir}/man1/stellarium.1"

%__install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%__install -D -m0644 "%{SOURCE2}" "%{buildroot}%{_datadir}/pixmaps/%{name}.png"
%suse_update_desktop_file -r "%{name}" Education Astronomy

%find_lang "%{name}"

%clean
%__rm -rf "%{buildroot}"

%files -f "%{name}.lang"
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/stellarium
%doc %{_mandir}/man1/stellarium.1*
%dir %{_datadir}/stellarium
%dir %{_datadir}/stellarium/data
%{_datadir}/stellarium/data/*
%dir %{_datadir}/stellarium/landscapes
%{_datadir}/stellarium/landscapes/*
%dir %{_datadir}/stellarium/nebulae
%{_datadir}/stellarium/nebulae/*
%dir %{_datadir}/stellarium/scripts
%{_datadir}/stellarium/scripts/*
%dir %{_datadir}/stellarium/skycultures
%{_datadir}/stellarium/skycultures/*
%dir %{_datadir}/stellarium/stars
%{_datadir}/stellarium/stars/*
%dir %{_datadir}/stellarium/textures
%{_datadir}/stellarium/textures/*
%{_datadir}/applications/stellarium.desktop
%{_datadir}/pixmaps/stellarium.png

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
