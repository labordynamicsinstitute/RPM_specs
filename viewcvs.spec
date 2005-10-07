#
# spec file for package viewcvs (Version 1.1.3)
#

Name:         viewcvs-alt
Version:      1.0
Release:      25
#
%define	apache_sysconfdir	/etc/apache2
#
%define site_python	%(python -c "import distutils.sysconfig; print distutils.sysconfig.get_python_lib()")
#
%define viewcvs_dir /srv/viewcvs-alt
%define viewcvs_altnum 3
%define mydocdir %_defaultdocdir/%name
#
Requires:     subversion-python
Provides:     subversion-viewcvs
#Obsoletes:    subversion-viewcvs
Group:        Development/Tools/Version Control
Summary:      ViewCVS - Browse a Subversion Repository with a Web Browser (alternate installation path)

BuildRoot:    %{_tmppath}/%{name}-%{version}-build
License:      Other License(s), see package, Apache
Group:        Development/Tools/Version Control
URL:          http://subversion.tigris.org
Source0:      subversion.viewcvs-cvs.tar.bz2
Source1:      subversion.viewcvs.conf
#
# build fixes
#
Patch42:      subversion.viewcvs-buglink.patch
#

%description
ViewCVS can browse directories, change logs, and do specific revisions
of files. It can display diffs between versions and show selections of
files based on tags or branches. In addition, ViewCVS has "annotation"
or "blame" support, Bonsai-like query facilities, template-based page
generation, and support for individually configurable virtual hosts. It
also includes support for CvsGraph -- a program to graphically display
the revision trees and branches.



Authors:
--------
    The ViewCVS Group:
        * Greg Stein
        * Tanaka Akira
        * Tim Cera
        * Peter Funk
        * Jay Painter

# multi-package setup
%package 2
Group:        Development/Tools/Version Control
Summary:      ViewCVS - Browse a Subversion Repository with a Web Browser (alternate installation path ALT2)
%description 2
See description of viewcvs-alt.

%package 3
Group:        Development/Tools/Version Control
Summary:      ViewCVS - Browse a Subversion Repository with a Web Browser (alternate installation path ALT3)
%description 3
See description of viewcvs-alt.

# additional version can be added here, see also %install and %files

#------------------------------ prep section ------------------------------
%prep
%setup -n viewcvs-cvs
#
%patch42

#------------------------------ build section ------------------------------
%build

#------------------------------ install section ------------------------------
%install
rm -rf $RPM_BUILD_ROOT
##
## viewcvs
mkdir -p $RPM_BUILD_ROOT/%{apache_sysconfdir}/conf.d
i=1
while [[ $i -le %{viewcvs_altnum} ]]
do
 cp -av %{S:1} $RPM_BUILD_ROOT/%{apache_sysconfdir}/conf.d/subversion.%{name}$i.conf
#
 ./viewcvs-install --prefix "%{viewcvs_dir}$i" --destdir "$RPM_BUILD_ROOT"
sed '
s@^#docroot.*@docroot = /viewcvs-docroot@
s@^default_root.*@default_root = your_unnamed_project@
s@^cvsgraph_conf.*@cvsgraph_conf = %{viewcvs_dir}/${i}cvsgraph.conf@
s@^hr_funout.*@hr_funout = 1@
s@^show_changed_paths.*@show_changed_paths = 0@
/^cvs_roots/,/^$/s/^/###/
/^#svn_roots/,/^$/c\
svn_roots:\
	your_unnamed_project : /srv/svn/repos/<your_unnamed_project> , \
	another_project : /srv/svn/repos/<another_project> \
#
' < viewcvs.conf.dist > $RPM_BUILD_ROOT%{viewcvs_dir}$i/viewcvs.conf
diff -up viewcvs.conf.dist $RPM_BUILD_ROOT%{viewcvs_dir}$i/viewcvs.conf || true
#
find $RPM_BUILD_ROOT%{viewcvs_dir}$i -type d | \
sed "s@$RPM_BUILD_ROOT@%dir @" > files.subversion.viewcvs$i
find $RPM_BUILD_ROOT%{viewcvs_dir}$i -type f | \
sed "s@$RPM_BUILD_ROOT@@;/\/templates\/\|\.conf$/s@^@%config (noreplace) @" >> files.subversion.viewcvs$i
let i+=1
done
#
#
#
##

%files  -f files.subversion.viewcvs1
%defattr(-,root,root)
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/subversion.%{name}1.conf

%files 2 -f files.subversion.viewcvs2
%defattr(-,root,root)
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/subversion.%{name}2.conf

%files 3 -f files.subversion.viewcvs3
%defattr(-,root,root)
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/subversion.%{name}3.conf


%changelog -n subversion
* Fri Mar 04 2005 - olh@suse.de
- restore old java checks
* Thu Mar 03 2005 - olh@suse.de
- update cvs2svn to version 1.2.1, rev r1422
  * Fix cvs2svn's dumpfile output to work after Subversion's r12645.
  will also improve conversion speed
* Wed Feb 23 2005 - olh@suse.de
- build swig-pl without make -jN to avoid broken dependencies
* Tue Feb 22 2005 - ro@suse.de
- search also for "other" java on a biarch platform
* Sat Feb 19 2005 - olh@suse.de
- use lib macro to find java package
* Wed Feb 16 2005 - schwab@suse.de
- Don't override $EDITOR.
* Tue Feb 15 2005 - uli@suse.de
- cope with jpackage-compliant IBMJava2 (fixes s390*)
* Sun Jan 23 2005 - olh@suse.de
- set docroot=/viewcvs-docroot in viewcvs.conf
  handle SVN_VIEWCVS_MODPYTHON in apache2 subversion.viewcvs.conf
* Mon Jan 17 2005 - olh@suse.de
- update to 1.1.3
- update viewcvs and cvs2svn to current cvs/svn status
* Sat Jan 08 2005 - olh@suse.de
- update viewcvs, includes the DESTDIR patch
* Fri Jan 07 2005 - olh@suse.de
- build java bindings
* Thu Jan 06 2005 - olh@suse.de
- update to 1.1.2
  drop subversion-keywords_on_add.patch
  http://svnbook.red-bean.com/svnbook-1.1/ch07s02.html#svn-ch-7-sect-2.4
- add 2 security patches for viewcvs
  subversion.viewcvs.forbidden-hide_cvsroot_CAN-2004-0915.patch (#48989)
  subversion.viewcvs.escapeurl_CAN-2004-1062.patch (#49086)
- update to docbook-xsl-1.67.2.tar.gz
- update viewcvs and cvs2svn to current cvs/svn status
- rename subversion-cvs2svn to cvs2svn
- rename subversion-viewcvs to viewcvs
* Thu Oct 14 2004 - olh@suse.de
- update to 1.0.9
  User-visible-changes:
- Server:
  * fixed: 'svn ls' HTTP performance regression
  * fixed: 'svn log -v' hiding too much info on 'empty' revisions.
* Thu Oct 14 2004 - ro@suse.de
- added libgcrypt, libgpg-error to neededforbuild
* Fri Sep 24 2004 - olh@suse.de
- update to 1.0.8
  CAN-2004-0749: mod_authz_svn fails to protect metadata (#45610)
  Version 1.0.8
  User-visible-changes:
  * fixed: mod_authz_svn path and log-message metadata leaks.
  Version 1.0.7
  User-visible-changes:
  * fixed: 'svn st -u' crash (r10841)
  * fixed: potential repos corruption; ensure stdin/out/err always open
  * fixed: allow propnames containing ":" to be fetched via http://
  * fixed: allow user to interrupt between authentication prompts
  * fixed: work around +t directory-creation bug in APR
  * various small fixes to Book
  Developer-visible changes:
  * fix library dependencies for bindings
  * perl bindings: various fixes
* Wed Sep 01 2004 - olh@suse.de
- add psvn.el
* Fri Aug 27 2004 - olh@suse.de
- update cvs2svn to 1.0.0 status, rev 1368
  update viewcvs to todays status
* Mon Aug 09 2004 - olh@suse.de
- update cvs2svn to 1.0rc4 status, rev 1322
  update viewcvs to todays status
  update to docbook-xsl-1.65.1.tar.gz
* Tue Aug 03 2004 - olh@suse.de
- build perl bindings, allow make -jN
* Thu Jul 29 2004 - poeml@suse.de
- fix path in README.SuSE
- fix fillup of /etc/sysconfig/svnserve
* Tue Jul 27 2004 - olh@suse.de
- update to rev 10424 from 1.0.x branch, 1.0.6 status
* Tue Jul 06 2004 - poeml@suse.de
- add subversion.viewcvs-buglink.patch from James Henstridge, plus
  re.I modifier to match case insensitively
* Tue Jul 06 2004 - poeml@suse.de
- update cvs2svn to r1214
- update viewcvs to current CVS snapshot
* Mon Jul 05 2004 - poeml@suse.de
- fix "select for diff" in viewcvs (patch by Heinrich
  Stamerjohanns)
* Mon Jun 14 2004 - olh@suse.de
- update to rev 9955 from 1.0.x branch, 1.0.5 status
* Mon May 10 2004 - olh@suse.de
- remove Requires: -<release> (#40278)
* Sun May 09 2004 - olh@suse.de
- add subversion-1.0.1-exploit-old_timestamp_format.patch (#39774)
* Mon Apr 19 2004 - olh@suse.de
- update to rev 9429 from 1.0.x branch, 1.0.2 status
* Mon Mar 08 2004 - olh@suse.de
- update to rev 8925 from 1.0.x brancht, almost 1.0.1 status
* Thu Mar 04 2004 - poeml@suse.de
- add patch for ViewCVS
  http://cvs.sourceforge.net/viewcvs.py/viewcvs/viewcvs/lib/ezt.py?r1=1.22&r2=1.23
* Mon Mar 01 2004 - olh@suse.de
- update to rev 8871 from 1.0.x branch
* Sun Feb 22 2004 - olh@suse.de
- update to 0.99.0 (1.0.0-beta1), from 1.0.x branch, rev 8806
* Sat Jan 24 2004 - olh@suse.de
- update to 0.37.0 from 1.0-stabilization branch
  allow swig 1.3.21
* Mon Sep 08 2003 - poeml@suse.de
- subversion-viewcvs: explicitely allow access to the
  /srv/viewcvs/www/cgi directory, because we can not take it for
  granted that apache2 allows it by default [#29729]
* Fri Aug 29 2003 - poeml@suse.de
- README.SuSE: add documentation on file permissions; fold in
  feedback from Heinrich Stamerjohanns
* Fri Aug 29 2003 - mcihar@suse.cz
- subversion-cvs2svn requires python
* Wed Aug 27 2003 - olh@suse.de
- do not install the book.pdf
* Mon Aug 18 2003 - olh@suse.de
- update to 0.27.0, revision 6740
  update viewcvs to todays cvs status
* Sun Aug 10 2003 - olh@suse.de
- update to pre 0.27, revision 6695
* Sun Aug 10 2003 - olh@suse.de
- add rcsvnserve
  update hook template, svnlook is in /usr/bin
  update viewcvs to todays cvs status
* Wed Jul 30 2003 - poeml@suse.de
- get CFLAGS from apxs, so they match the ones that apr and apache2
  were built with
- "make external-install local-install" targets instead of make
  install, to work avoid hard coded pulling of the revision number
  from the svn working copy in the revision-install target
* Fri Jul 25 2003 - olh@suse.de
- update to 0.26.0, revision 6576
* Sun Jul 20 2003 - olh@suse.de
- split packages subversion-doc and subversion-viewcvs
  use SVN_DOC instead of SVN_DOCU
  use SVN_VIEWCVS to enable the scriptalias
* Sat Jul 12 2003 - olh@suse.de
- update to 0.25.0, revision 6456
  use SVN_DOCU to provide html documentation via apache2
* Sat Jul 05 2003 - olh@suse.de
- add subversion-python_bytecode-path-pr1131.patch
  do not compile in RPM_BUILD_ROOT, use builddir instead
* Tue Jun 17 2003 - olh@suse.de
- update to 0.24.1 final, revision 6254
  update svnbook.red-bean.com/book.pdf
* Tue Jun 17 2003 - kukuk@suse.de
- Add missing directory to filelist
* Mon May 19 2003 - olh@suse.de
- update to 0.23.0 final, revision 5981
  add subversion-infopages.patch
* Sat May 10 2003 - olh@suse.de
- update to 0.22.1 final, revision 5877
  use apache-2.0.45 apr
* Fri May 02 2003 - olh@suse.de
- update to 0.22.0 , revision 5780
  build with newer apr
* Fri Apr 11 2003 - ro@suse.de
- fix deprecated head/tail calling syntax (-1)
* Wed Mar 19 2003 - olh@suse.de
- update to 0.19.1 , revision 5394
* Sun Mar 16 2003 - olh@suse.de
- update to 0.19.1 , revision 5349
  update book.pdf
* Tue Feb 18 2003 - poeml@suse.de
- python might live below /usr/lib64
* Thu Feb 13 2003 - olh@suse.de
- update to 0.17.1 , revision 4877
  finally a working cvs2svn version, use the cvs2svn-mmacek branch
* Mon Feb 10 2003 - poeml@suse.de
- remove hints about SuSEconfig, it's not needed. Add README.SuSE
  about server configuration
- drop /etc/apache2/modules/subversion, it is no longer needed
- MPM specific links to mod_dav_svn.so are no longer needed
- server requires apache2, and a Require on apr is no longer valid
* Mon Feb 10 2003 - olh@suse.de
- split packages cvs2svn and tools
* Thu Feb 06 2003 - olh@suse.de
- add hint about SuSEconfig run in subversion.conf example
* Sun Feb 02 2003 - olh@suse.de
- add subversion-0.17.1-editor.diff
  subversion-0.17.1-keywords_on_add.diff
* Tue Jan 28 2003 - olh@suse.de
- add subversion book.pdf from the website
  add svnserve and svnversion
  remove outdated info docu
  build and add html documentation
  new apache2 config file format, extend example in subversion.conf
* Wed Jan 22 2003 - olh@suse.de
- update to 0.17.1 , revision 4508
* Tue Jan 21 2003 - olh@suse.de
- update to 0.17.0 , revision 4474
* Thu Dec 05 2002 - poeml@suse.de
- update to 0.16.0 , revision 3987
- use macro <apache2-devel-packages> in #neededforbuild
- get rid of hardcoded MPM names
* Wed Dec 04 2002 - olh@suse.de
- update to 0.15.0 , revision 3985
* Mon Nov 11 2002 - ro@suse.de
- changed neededforbuild <xshared> to <x-devel-packages>
- changed neededforbuild <xdevel> to <>
* Sun Oct 13 2002 - olh@suse.de
- update to 0.14.3 , revision 3360
  add subversion configfiles for apache2
* Sat Oct 12 2002 - olh@suse.de
- update to 0.14.3 , revision 3353
  add more dir path to file list, add more docu
  apxs is in /usr/sbin
* Thu Sep 19 2002 - olh@suse.de
- update to 0.14.3 , revision 3188
  use python-imaging instead of python-tkinter
* Sat Aug 31 2002 - poeml@suse.de
- update to last release 0.14.2 (svn update was broken when
  repositories contained renames)
* Tue Aug 27 2002 - poeml@suse.de
- use apxs2, building a common mod_dav_svn.so for all three MPMs
- don't let apxs add an entry for mod_dav_svn.so into httpd.conf
* Sun Aug 11 2002 - olh@suse.de
- update to 0.14.1, rev 2935, build html docs
* Thu Aug 01 2002 - olh@suse.de
- update to 2840, add svnadmin and svnlock
* Tue Jul 30 2002 - olh@suse.de
- remove apr, use apache2 instead, update to 2787
* Fri Jul 26 2002 - olh@suse.de
- initial SuSE release with version 0.14.0.2720
  built with apr_20020725163531 and apr-util-20020725
