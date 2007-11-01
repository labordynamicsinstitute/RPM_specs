#
# spec file for package octave (Version 2.9.12)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
# usedforbuild    Mesa SDL aaa_base aalib acl atk attr audiofile audit-libs autoconf automake bash binutils bzip2 cairo coreutils cpio cpp cpp42 cracklib cups-libs cvs dejagnu diffutils esound expect file filesystem fillup findutils fontconfig freetype2 gawk gcc gcc-c++ gcc-fortran gcc42 gcc42-c++ gcc42-fortran gd gdbm gettext gettext-devel ghostscript-fonts-std ghostscript-library ghostscript-x11 glib2 glibc glibc-devel glibc-locale glitz gmp gmp-devel gnuplot gperf gpm grep groff gtk2 gzip hicolor-icon-theme info insserv less libacl libasound2 libattr libbz2-1 libbz2-devel libdb-4_5 libdrm libexpat1 libgcc42 libgfortran42 libgimpprint libgomp42 libjpeg libltdl-3 libmspack libmudflap42 libopenssl0_9_8 libpng libreadline5 libstdc++42 libstdc++42-devel libtiff3 libtool libuuid1 libvolume_id libxcrypt libxml2 libzio linux-kernel-headers m4 make man mktemp mpfr ncurses ncurses-devel net-tools netcfg openssl-certs pam pam-modules pango patch perl perl-Tk perl-base permissions plotutils poppler popt readline-devel rpm sed sysvinit t1lib tar tcl tcpd termcap texinfo texlive texlive-bin texlive-bin-latex texlive-latex timezone util-linux wxGTK xaw3d xorg-x11-libICE xorg-x11-libSM xorg-x11-libX11 xorg-x11-libXau xorg-x11-libXext xorg-x11-libXfixes xorg-x11-libXmu xorg-x11-libXp xorg-x11-libXpm xorg-x11-libXprintUtil xorg-x11-libXrender xorg-x11-libXt xorg-x11-libXv xorg-x11-libfontenc xorg-x11-libs xorg-x11-libxcb xorg-x11-libxkbfile zlib

Name:           octave
BuildRequires:  dejagnu gcc-c++ gcc-g77 gmp gnuplot gperf readline-devel termcap te_latex
URL:            http://www.octave.org/
License:        GPL v2 or later
Group:          Productivity/Scientific/Math
Provides:       matlab4
Requires:       gnuplot gcc-fortran texinfo
PreReq:         %install_info_prereq
Autoreqprov:    on
Version:        2.9.12
Release:        27
Summary:        A High Level Programming Language
Source:         %{name}-%{version}.tar.bz2
Patch:          octave-%{version}-gcc-4.1.diff
Patch1:         %{name}-%{version}_without-randlib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define       regenerate 1
%define       check	 	0

%description
Octave is a high level programming language. It is designed for the
solution of numeric problems. There is a command line interface
supplied.



Authors:
--------
    John W. Eaton <jwe@bevo.che.wisc.edu>
    
    Randlib:
    venier@odin.mdacc.tmc.edu, bwb@odin.mdacc.tmc.edu

%debug_package
%package devel
Summary:        Development files for octave
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.



Authors:
--------
    John W. Eaton <jwe@bevo.che.wisc.edu>

%prep
%setup -q
%patch
%patch1

%build
mkdir m4
mv aclocal.m4 m4/octave.m4
%{suse_update_config -f . scripts}
aclocal --force --verbose -I m4
#aclocal
autoconf -f --verbose
#autoreconf --force --verbose
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fno-strict-aliasing" \
CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fno-strict-aliasing" \
FFLAGS="-Os" \
	./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--libexecdir=%{_libdir} \
	--libdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-rpath \
	--disable-static \
	--enable-dl \
	--enable-lite-kernel
rm -rf libcruft/ranlib  #without randlib
echo Building octave...
# regenerate info files
touch doc/conf.texi
#parallel building fails on some/all architectures
make #%{?jobs:-j%jobs}
%if %check
make check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/
install -d $RPM_BUILD_ROOT/%_infodir 
install -d $RPM_BUILD_ROOT/%_mandir
make DESTDIR=$RPM_BUILD_ROOT install
#     exec_prefix=$RPM_BUILD_ROOT/usr \
#     libdir=$RPM_BUILD_ROOT/%_libdir \
#     libexecdir=$RPM_BUILD_ROOT/%_libdir \
#     prefix=$RPM_BUILD_ROOT/usr \
#     mandir=$RPM_BUILD_ROOT/%_mandir \
#     infodir=$RPM_BUILD_ROOT/%_infodir \
#     install 
#install -m 644 doc/faq/*.info $RPM_BUILD_ROOT%{_infodir}
#install -m 644 doc/liboctave/*.info $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/%{_libdir}/octave/ls-R > xtmp
mv xtmp $RPM_BUILD_ROOT/%{_libdir}/octave/ls-R
sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/usr/share/octave/ls-R > xtmp
mv xtmp $RPM_BUILD_ROOT/usr/share/octave/ls-R
#sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/usr/include/octave-2.9.12/octave/defaults.h > xtmp
#mv xtmp $RPM_BUILD_ROOT/usr/include/octave-2.9.12/octave/defaults.h
#sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/usr/include/octave-2.9.12/octave/oct-conf.h > xtmp
#mv xtmp $RPM_BUILD_ROOT/usr/include/octave-2.9.12/octave/oct-conf.h
#sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_DIR/src/defaults.h > xtmp
#mv xtmp $RPM_BUILD_DIR/src/defaults.h
ln -s %{_infodir}/octave.info-1.gz $RPM_BUILD_ROOT/%{_infodir}/octave.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
#%install_info --info-dir=%{_infodir} %{_infodir}/Octave-FAQ.info.gz
#%install_info --info-dir=%{_infodir} %{_infodir}/liboctave.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%postun
/sbin/ldconfig
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/Octave-FAQ.info.gz
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/liboctave.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%files
%defattr(-,root,root)
%doc COPYING NEWS README THANKS PROJECTS doc/ChangeLog
%doc doc/faq/Octave-FAQ.{dvi,ps} doc/interpreter/octave.{dvi,ps}
%doc doc/refcard/refcard-a4.{dvi,ps}
/usr/bin/mkoctfile*
/usr/bin/octave-bug*
/usr/bin/octave
/usr/bin/%{name}-%{version}
%doc %{_infodir}/*.gz
%doc %{_mandir}/man1/octave.1.gz
%doc %{_mandir}/man1/octave-bug.1.gz
%_libdir/octave*
/usr/share/octave/

%files devel
%defattr(-,root,root)
/usr/include/*
/usr/bin/*-config*
%doc %{_mandir}/man1/octave-config.1.gz
%doc %{_mandir}/man1/mkoctfile.1.gz
%doc doc/liboctave/liboctave.{dvi,ps} 

%changelog
* Wed Jul 25 2007 - pgajdos@suse.cz
- supressed paralell building which fails at least on some
  architectures
* Wed Jul 11 2007 - pgajdos@suse.cz
- updated to 2.9.12 and removed randlib [#279883]
- without-randlib.patch
* Thu Jun 21 2007 - pgajdos@suse.cz
- added texinfo to Requires
* Fri May 25 2007 - pgajdos@suse.cz
- made subpackage octave-devel
* Sat Apr 21 2007 - aj@suse.de
- Use texlive.
* Thu Jun 22 2006 - ro@suse.de
- remove selfprovides
* Wed May 24 2006 - anicka@suse.cz
- update to 2.1.73
  - bugfix release
* Mon Feb 13 2006 - anicka@suse.cz
- require gcc-fortran (fixes #150047)
* Wed Feb 01 2006 - anicka@suse.cz
- add -Os to FFLAGS (fixes #136787)
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 14 2006 - kukuk@suse.de
- Add gmp-devel to nfb
* Thu Jan 05 2006 - anicka@suse.cz
- update to 2.1.72
* Mon Nov 14 2005 - anicka@suse.cz
- fix build (gcc 4.1)
* Tue Nov 01 2005 - anicka@suse.cz
- fix build (move code around in CMatrix.cc)
* Tue Jun 28 2005 - anicka@suse.cz
- update to 2.1.71
* Wed May 11 2005 - ro@suse.de
- fix build with gcc4
* Mon Apr 18 2005 - mcihar@suse.de
- GNU Fortran 77 compiler now requires gmp, let's add it
- still doesn't compile, because GCC: TODO: Functions with alternate entry points
* Tue Dec 21 2004 - mcihar@suse.cz
- update to 2.1.64
- do not include info pages, as they are out of date
- string patching was not needed for long time, so drop the patch
* Thu Nov 11 2004 - ro@suse.de
- fixed file list
* Wed Aug 04 2004 - mcihar@suse.cz
- update to 2.1.57
* Fri Mar 05 2004 - mcihar@suse.cz
- really compile with -fno-strict-aliasing
- doesn't need f2c at all
* Fri Mar 05 2004 - mcihar@suse.cz
- update to 2.1.55
- fix info pages installation
- add some docs
- use -fno-strict-aliasing
* Fri Jan 09 2004 - adrian@suse.de
- add %%run_ldconfig
- use RPM_OPT_FLAGS
* Fri Aug 29 2003 - mcihar@suse.cz
- info pages should not be executable
* Wed Aug 13 2003 - ro@suse.de
- fix info page installation again (thanks to DJurzitza)
* Wed Jul 30 2003 - ro@suse.de
- install more info pages
* Thu Jun 26 2003 - ro@suse.de
- remove traces of buildroot from installed files
* Wed Jun 11 2003 - ltinkl@suse.cz
- updated sources to version 2.1.49
* Thu Apr 24 2003 - ro@suse.de
- fix install_info --delete call and move from preun to postun
* Mon Mar 03 2003 - ro@suse.de
- added info dir entries
* Tue Feb 25 2003 - mcihar@suse.cz
- removed -mminimal-toc as it is now part of RPM_OPT_FLAGS for ppc64
- added gnuplot to requires
* Mon Feb 10 2003 - mcihar@suse.cz
- used %%install_info macro (fixes bug #23443)
* Wed Feb 05 2003 - mcihar@suse.cz
- removed RPM_OPT_FLAGS="$RPM_OPT_FLAGS -mminimal-toc" for ppc64
  (fixes bug #23266)
- updated to 2.1.44
* Fri Nov 22 2002 - mcihar@suse.cz
- updated to 2.1.40, mostly only configure and automake fixes, it
  also fixes sstream and some other smaller issues with gcc 3.3
- fixed multiline string
* Tue Aug 06 2002 - mcihar@suse.cz
- updated to 2.1.36
* Sat Jun 29 2002 - olh@suse.de
- build with -mminimal-toc on ppc64, use RPM_OPT_FLAGS for CFLAGS
* Tue May 21 2002 - ro@suse.de
- call suse_update_config also for kpathsea subdir
* Wed May 08 2002 - ro@suse.de
- fix for latest gcc-snapshot
* Fri Apr 19 2002 - coolo@suse.de
- updating to octave 2.1.35 as octave 2.0.1[67] were hopeless
  with gcc 3.1 (gave up after 2 days of work)
* Tue May 08 2001 - mfabian@suse.de
- bzip2 sources
* Fri May 05 2000 - bubnikv@suse.cz
- added buildroot
- /usr/execlib/octave moved to /usr/lib/octave according to FHS 2.1
* Mon Feb 21 2000 - ro@suse.de
- update to 2.0.16
* Tue Jan 25 2000 - ro@suse.de
- update to 2.0.15
- man,info to /usr/share using macro
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Jul 14 1999 - ro@suse.de
- update to 2.0.14
* Thu May 20 1999 - ro@suse.de
- use CFLAGS="-D_GNU_SOURCE"
* Mon Nov 23 1998 - ro@suse.de
- update to 2.0.13 / builds with glibc
* Wed Oct 07 1998 - ro@suse.de
- BETA: added f2c to neededforbuild
* Wed Jan 28 1998 - ro@suse.de
- removed libhistory.so & libreadline.so as well and link static
  to these
* Mon Nov 17 1997 - bs@suse.de
- removed libhistory.a & libreadline.a from file list.
* Wed Nov 12 1997 - ro@suse.de
- minor changes in specfile
  setting host to ARCH-suse-linux
* Mon Nov 10 1997 - ro@suse.de
- new version 2.0.9
* Tue Oct 07 1997 - ro@suse.de
- prepared spec file
- added README-GCC-2.7.? patches
