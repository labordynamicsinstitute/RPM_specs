#
# spec file for package sqlite (Version 3.4.1)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           sqlite
BuildRequires:  gcc-c++ readline-devel tcl-devel
%if %{?suse_version:1}%{?!suse_version:0}
BuildRequires:  update-desktop-files
%endif
License:        Public Domain, Freeware
Group:          Productivity/Databases/Servers
Summary:        Embeddable SQL Database Engine
URL:            http://www.sqlite.org/
Version:        3.4.1
Release:        5.4
Source0:        http://www.sqlite.org/%name-%version.tar.bz2
Source1:        sqlite.desktop
Source2:        sqlite-check_fsync_dir.c
Patch0:         %name.diff
Patch2:         %{name}-test-notime.diff
Patch3:         fix-64bit.diff
Patch5:         fix-64bit-3.diff
Patch7:         sqlite-load-ext.diff
Patch8:         disable-check.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command line tool or via any
application that supports the Qt database plug-ins.



Authors:
--------
    D. Richard Hipp <drh@hwaci.com>

%package tcl
Group:          Development/Libraries/Tcl
Summary:        Tcl binding for SQLite

%description tcl
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

This package contains an extension for the Tcl programming language to
access SQLite databases.



Authors:
--------
    D. Richard Hipp <drh@hwaci.com>

%package devel
Group:          Productivity/Databases/Servers
Summary:        Embeddable SQL Database Engine
Requires:       %name = %version glibc-devel

%description devel
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server; SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command-line tool or via any
application which supports the Qt database plug-ins.



Authors:
--------
    D. Richard Hipp <drh@hwaci.com>

%prep
%setup -q
%patch0
%patch2
%ifarch x86_64 ppc64 s390x ia64 mips64
%patch3
%endif
%patch5
%patch7
%patch8
# does not work due to our ulimits in our build system
rm test/bigfile.test
autoreconf -f -i

%build
  export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG=1 -O3"
  export CXXFLAGS="$CFLAGS"
  mkdir build
  cd build
  cp ../VERSION .
  ../configure \
    --prefix=/usr \
    --libdir=%_libdir \
    --mandir=%_mandir \
    --enable-threadsafe \
    --enable-releasemode \
    --enable-tempstore=yes \
    --sysconfdir=/etc/
  make
  make doc
  #
  # check if fsync() on directories works with the current file
  # system, and skip the test suite if it doesn't.
  # As of this writing, fsync() fails on directories inside tmpfs.
  #
  gcc %optflags -o check_fsync_dir %SOURCE2
  if ./check_fsync_dir; then
       make fulltest
  fi

%install
  cd build
  make install \
        DESTDIR="$RPM_BUILD_ROOT" \
        tclscriptdir=%tclscriptdir \
        tcllibdir=%_libdir
  install -d $RPM_BUILD_ROOT%_mandir/man1/
  install -m 0644 ../sqlite3.1 $RPM_BUILD_ROOT%_mandir/man1/
#%if %{?suse_version:1}%{?!suse_version:0}
#  sed -i 's,%buildroot,,' %buildroot/%tclscriptdir/sqlite*/pkgIndex.tcl
#%endif
  #
  # install the susehelp meta file
  mkdir -p $RPM_BUILD_ROOT/usr/share/susehelp/meta/Development/Libraries/
  install -m 0644 %SOURCE1 \
        $RPM_BUILD_ROOT/usr/share/susehelp/meta/Development/Libraries/
%if %{?suse_version:1}%{?!suse_version:0}
  %suse_update_desktop_file $RPM_BUILD_ROOT/usr/share/susehelp/meta/Development/Libraries/%name.desktop
%endif

%clean
  rm -rf $RPM_BUILD_ROOT

%pre -p /sbin/ldconfig

%post -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/bin/sqlite3
%_mandir/man1/*
%_libdir/libsqlite*.so.*

%files tcl
%defattr(-,root,root)

%tclscriptdir

%files devel
%defattr(-,root,root)
%doc build/doc/*
%doc /usr/share/susehelp
/usr/include/*.h
%_libdir/libsqlite*.a
%_libdir/libsqlite*.la
%_libdir/libsqlite*.so
%_libdir/pkgconfig/sqlite3.pc

%changelog
* Mon Aug 13 2007 adrian@suse.de
- call %%post/%%pre ldconfig again (#298292)
* Mon Aug  6 2007 adrian@suse.de
- update to version 3.4.1
  * Bugfix release to solve database corruption
  * remove static fts2 plugin patch, it is broken and get not used
  * Changelog from the release:
  - Fix a bug in VACUUM that can lead to  database corruption if two
    processes are connected to the database at the same time and one
    VACUUMs then the other then modifies the database.
  - The expression "+column" is now considered the same as "column" when
    computing the collating sequence to use on the expression.
  - In the TCL language interface, "@variable" instead of "$variable" always
    binds as a blob.
  - Added PRAGMA freelist_count for determining the current size of the
    freelist.
  - The  PRAGMA auto_vacuum=incremental setting is now persistent.
  - Add FD_CLOEXEC to all open files under unix.
  - Fix a bug in the  min()/max() optimization when applied to descending
    indices.
  - Make sure the TCL language interface works correctly with 64-bit integers
    on 64-bit machines.
  - Allow the value -9223372036854775808 as an integer literal in SQL
    statements.
  - Add the capability of "hidden" columns in virtual tables.
  - Use the macro SQLITE_PRIVATE (defaulting to "static") on all internal
    functions in the amalgamation.
  - Add pluggable tokenizers and ICU tokenization support to FTS2
  - Other minor bug fixes and documentation enhancements
* Tue Jun 26 2007 adrian@suse.de
- update to version 3.4.0
  WARNING: this version might cause incompatibilities due to new
    limits. These limits could be raised again, if we run in
    trouble, but let's follow upstream for now.
  * Two important bugfixes for database corruption.
  * New features like incremental BLOB I/O and incremental vacuum
* Fri Apr 27 2007 adrian@suse.de
- update to version 3.3.17
  * bug fix in forwards-compatibility logic of SQLite
* Thu Apr 19 2007 adrian@suse.de
- update to version 3.3.16
  * speed improvements were not enabled in .15 by accident
* Mon Apr 16 2007 adrian@suse.de
- update to version 3.3.15
  * speed improvements
  * new exclusive locking mode
- switch to -O3 now
- general spec file clean up
* Mon Feb 19 2007 adrian@suse.de
- update to version 3.3.13
  from the changelog:
  * Add a "fragmentation" measurement in the output of sqlite3_analyzer.
  * Add the COLLATE operator used to explicitly set the collating
    sequence used by an expression. This feature is considered
    experimental pending additional testing.
  * Allow up to 64 tables in a join - the old limit was 32.
  * Added two new experimental functions: randomBlob() and hex().
    Their intended use is to facilitate generating UUIDs.
  * Fix a problem where PRAGMA count_changes was causing incorrect
    results for updates on tables with triggers
  * Fix a bug in the ORDER BY clause optimizer for joins where
    the left-most table in the join is constrained by a UNIQUE index.
  * Fixed a bug in the "copy" method of the TCL interface.
  * Bug fixes in fts1 and fts2 modules.
* Mon Feb 12 2007 dmueller@suse.de
- fix library dependencies after loadable extensions were enabled
* Tue Feb  6 2007 dmacvicar@suse.de
- Enable support for loadable extensions
* Mon Feb  5 2007 max@suse.de
- Enable the fts1 and fts2 modules and link them in statically.
* Wed Jan 31 2007 adrian@suse.de
- update to version 3.3.12
  * further bugfixes, esp. for bugs introduced in 3.3.9
* Thu Jan 11 2007 adrian@suse.de
- update to version 3.3.10
  * pure bug fix release
* Tue Jan  9 2007 adrian@suse.de
- update to version 3.3.9
  * fixes database corruption "under obscure and difficult to
    reproduce circumstances".
  * new sqlite3_prepare v2() api (new header file)
* Mon Nov  6 2006 adrian@suse.de
- fix permissions of installed man page
* Mon Oct 16 2006 adrian@suse.de
- update to version 3.3.8
  * full-text search using the FTS1 module
  * minor bufixes
- two testcases got disabled, because they fail.
  We need to review the reason for that before shipping this package,
  but this package builds again at least.
* Wed Aug 23 2006 adrian@suse.de
- update to version 3.3.7
  * support for loadable extensions and virtual tables
  * minor bugfixes
* Thu May 18 2006 adrian@suse.de
- update to version 3.3.5
  Version 3.3 adds support for CHECK constraints, DESC indices,
  separate REAL and INTEGER column affinities, a new OS interface
  layer design, and many other changes.
  The file format for version 3.3 has changed slightly. SQLite 3.3
  will read and write legacy databases created with any prior
  version of SQLite 3. But databases created by version 3.3.0 will
  not be readable or writable by earlier versions of the SQLite
* Wed Mar 22 2006 schwab@suse.de
- Fix another 64bit bug.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan  9 2006 adrian@suse.de
- disable "same thread check". It is only needed with broken
  thread implementations and will be similar offered in sqlite 3.3
* Wed Jan  4 2006 adrian@suse.de
- update to version 3.2.8
  * bugfix release
* Tue Jan  3 2006 rguenthe@suse.de
- Correct 64bit issues causing x86_64 testsuite failures.
* Fri Dec  2 2005 jw@suse.de
- VERSION parsing back to normal.
  3002007 looks better than 3000000
* Mon Oct 24 2005 adrian@suse.de
- fix build for 64bit
* Mon Oct 17 2005 adrian@suse.de
- update to version 3.2.7
  * needed an additional fix for conflict.test
* Tue Aug 30 2005 jw@suse.de
- disabled a timing test. This fixes failed builds
  on heavy loaded autobuild hosts.
* Wed Jun 29 2005 jw@suse.de
- configure script fixed: VERSION was misparsed.
* Mon Jun 27 2005 max@suse.de
- Skip the testsuite if the underlaying file system doesn't
  support fsync() on directories (e.g. tmpfs).
* Tue Jun 21 2005 max@suse.de
- Update to version 3.2.2.
- Improved installation of the Tcl package.
* Thu Apr 21 2005 max@suse.de
- Disabling of certain tests for certain architectures does not
  seem to be needed anymore.
* Wed Apr 20 2005 ro@suse.de
- get patch to even apply
* Tue Apr 19 2005 max@suse.de
- Added a subpackage for the Tcl extension.
* Fri Apr  8 2005 adrian@suse.de
- update to version 3.2.1
* Tue Mar 29 2005 adrian@suse.de
- update to version 3.2.0
* Mon Feb 28 2005 adrian@suse.de
- update to version 3.1.3
  * a minor bugfix for VACUUM databases
  * to remain compatible with future 3.2 databases
- obsoletes a testsuite workaround
* Fri Feb 18 2005 adrian@suse.de
- fix library versioning
* Wed Feb 16 2005 adrian@suse.de
- update to version 3.1.2
  * contains a criticial bugsfix, which can corrupted the database
    when using the VACUUM command
* Mon Nov 29 2004 adrian@suse.de
- update to version 3.0.8
* Mon Nov 15 2004 adrian@suse.de
- add susehelp desktop file for developer documentation
* Mon Nov 15 2004 adrian@suse.de
- fix libdir path in .la file for lib64 systems
* Mon Oct 25 2004 adrian@suse.de
- enable utf-8 support
* Fri Jul 30 2004 adrian@suse.de
- run "make alltest"
* Thu Jul 29 2004 adrian@suse.de
- update to version 2.8.15
- disable wrong tcl test case on 64bit
* Mon Jun 21 2004 adrian@suse.de
- update to version 2.8.14
* Tue Jun  1 2004 adrian@suse.de
- package sqlite man page
* Fri Apr 23 2004 adrian@suse.de
- update to version 2.8.13
* Mon Mar  1 2004 adrian@suse.de
- disable format3 test case for ppc for now
* Sun Feb 29 2004 adrian@suse.de
- update to version 2.8.12
- add usual 64bit fixes
- add -fno-strict-aliasing
- disable bigfile test case due to limits in autobuild
* Thu Jan 22 2004 adrian@suse.de
- update to version 2.8.11
  * one testcase fails on ppc, our ppc people will have a look
* Mon Dec 29 2003 adrian@suse.de
- update to version 2.8.8
  * several 64 bit fixes have been merged, some more are needed now
- ignore some not exact matching float test cases on s390*
- enable threading support
* Tue Dec  2 2003 adrian@suse.de
- initial package of version 2.8.6
- a number of 64bit fixes
- some test cases got disabled, because they use an invalid Tcl
  Interface for 64bit
