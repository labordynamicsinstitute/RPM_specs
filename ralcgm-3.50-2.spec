Summary: ralcgm is a CGM viewer and can convert between cgm formats
Name: ralcgm
Version: 3.50
Release: 2
Copyright: Distributable
Group: Applications/Graphics
Url: http://www.bitd.clrc.ac.uk/Activity/RAL-CGM
Packager: James Henstridge <james@daa.com.au> (Rel 1), John Wingate <johnww@worldpath.net> (Rel 2)

Source: ftp://ftp.cc.rl.ac.uk/pub/graphics/ralcgm/unix/ralcgm-%{version}.tar.Z
Patch0: ralcgm-linux.patch
Patch1: ralcgm-cgmitext.patch

BuildRoot: /var/tmp/%{name}-root

%description
RAL-CGM is a program to Translate or Interpret CGM metafiles, either to a
different encoding (Binary, Character or Clear Text) or to view on a
terminal using X-Windows or to send to a plotter (PostScript or HPGL).

%prep
%setup -c
%patch0 -p1
%patch1 -p1

%build
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm
./CGMconfig linux << EOF
${RPM_BUILD_ROOT}%{_prefix}/bin
n
${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm

y
y
y
y
y
y
n
y
y
y
EOF
# munge the mach.h configuration file to point to the correct directory
# after installation
sed '/^#define DATADIR/s!".*"!"%{_prefix}/share/ralcgm/"!' < include/mach.h > include/mach.h.tmp
mv -f include/mach.h.tmp include/mach.h

# copy data files
cp data/* ${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm

cd src
# HACK to get round the fact that the data files must be installed
# to build the package. %{_prefix}/share/ralcgm will be deleted ...
rm -rf %{_prefix}/share/ralcgm
ln -s $RPM_BUILD_ROOT%{_prefix}/share/ralcgm %{_prefix}/share/
make ralcgm
# remove symlink
rm -f %{_prefix}/share/ralcgm
cd ..

# remove uneeded source data files ...
rm -f ${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm/*.hfs
rm -f ${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm/*.bfs

# set permissions correctly ...
chmod 644 ${RPM_BUILD_ROOT}%{_prefix}/share/ralcgm/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%install
# almost all install stuff done as part of the weird build process
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/man/man1
install docs/ralcgm.man ${RPM_BUILD_ROOT}%{_prefix}/man/man1/ralcgm.1
gzip ${RPM_BUILD_ROOT}%{_prefix}/man/man1/ralcgm.1

%files
%defattr(-,root,root)
%{_prefix}/bin/ralcgm
%{_prefix}/share/ralcgm/*
%{_prefix}/man/man1/ralcgm.1.gz

%doc README examples

%changelog
* Sat Aug 11 2001 John Wingate <johnww@worldpath.net>
- fixed off-by-one error

* Wed Sep 20 2000 James Henstridge <james@daa.com.au>
- Linux port 
