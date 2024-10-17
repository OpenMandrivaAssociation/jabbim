Name:       jabbim
Version:    0.5.1
Release:    2
Summary:    Jabber client for mere mortals

Group:      Networking/Instant messaging 
License:    GPLv2+
URL:        https://dev.jabbim.cz/jabbim
# The source was obtained from upstream SVN repository:
# svn export svn://dev.jabbim.cz/jabbim/tags/0.5.1 jabbim-0.5.1
# tar -cjf jabbim-0.5.1.tar.bz2 jabbim-0.5.1/
Source0:    jabbim-0.5.1.tar.bz2
Patch0:     jabbim-0.4-autoupdate-disable-notification.diff
Patch1:     jabbim-0.5.1-mdv-fix-log-in-unicode.patch
BuildArch:  noarch


BuildRequires:  python >= 2.5
BuildRequires:  desktop-file-utils
BuildRequires:	qt4-devel
Requires:   python >= 2.5
Requires:   python-qt4
Requires:   python-twisted-names
Requires:   python-twisted-web
Requires:   python-twisted-web2
Requires:   python-twisted-words
Requires:   python-sqlite2
Requires:   python-configobj
Requires:   python-OpenSSL



%description
Jabbim is a user-friendly Jabber (XMPP) client. Its goal is to make the modern
and useful Jabber services approachable to common users. It integrates well
with the advanced functionality provided by the Jabber server of the same name
(see http://www.jabbim.com). Jabbim is written in Python and Qt4.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/jabbim
%{_datadir}/applications/jabbim.desktop
%{_datadir}/icons/hicolor/*/apps/jabbim.png
%{_datadir}/icons/hicolor/scalable/apps/jabbim.svg
%{_datadir}/pixmaps/jabbim.png
%{_datadir}/pixmaps/jabbim.svg
%{_datadir}/jabbim

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p0
# Fix Makefile 
sed -i 's|lrelease-qt4|lrelease|g' Makefile


%build
make clean
%make PREFIX=%_prefix

%install
%__rm -rf %{buildroot}

%makeinstall_std


%clean
%__rm -rf %{buildroot}



%changelog
* Mon Jul 26 2010 John Balcaen <mikala@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 560832
- Update to 0.5.1
- drop Source1 (not used anymore & provided by upstream)
- drop patch1
- add a new patch1 to fix a log error handling with python-twisted 10.1 (from upstream)
- fix Makefile in the spec for lrelease
- clean spec
- add requires (python-twisted-web2,python-OpenSSL,python-configobj)

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.4.3-2mdv2010.0
+ Revision: 438014
- rebuild

* Mon Dec 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.3-1mdv2009.1
+ Revision: 314409
- Add Requires
- Fix groups
- import jabbim


* Sun Dec 15 2008 Nicolas Lecureuil <neoclust@mandriva.org>  0.4.3-1mdv2009.1
- Import Jabbim from Fedora spec file
