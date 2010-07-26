Name:       jabbim
Version:    0.5.1
Release:    %mkrel 1
Summary:    Jabber client for mere mortals

Group:      Networking/Instant messaging 
License:    GPLv2+
URL:        http://dev.jabbim.cz/jabbim
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

