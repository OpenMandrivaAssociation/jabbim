Name:       jabbim
Version:    0.4.3
Release:    %mkrel 1
Summary:    Jabber client for mere mortals

Group:      Applications/Internet
License:    GPLv2+
URL:        http://dev.jabbim.cz/jabbim
# The source was obtained from upstream SVN repository:
# svn export svn://dev.jabbim.cz/jabbim/tags/0.4.3 jabbim-0.4.3
# tar -cjf jabbim-0.4.3.tar.bz2 jabbim-0.4.3/
Source0:    jabbim-0.4.3.tar.bz2
Source1:    jabbim.in
Patch0:     jabbim-0.4-autoupdate-disable-notification.diff
Patch1:     jabbim-0.4-stringlists-in-QVariants.diff
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  python >= 2.5
BuildRequires:  desktop-file-utils

Requires:   python >= 2.5
Requires:   python-qt4
#Requires:   python-twisted-names
#Requires:   python-twisted-web
#Requires:   python-twisted-words
#Requires:   python-sqlite2
#Requires:   pyOpenSSL

%define jabbimdata %{_datadir}/jabbim

%description
Jabbim is a user-friendly Jabber (XMPP) client. Its goal is to make the modern
and useful Jabber services approachable to common users. It integrates well
with the advanced functionality provided by the Jabber server of the same name
(see http://www.jabbim.com). Jabbim is written in Python and Qt4.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/jabbim
%{_datadir}/applications/fedora-jabbim.desktop
%{_datadir}/icons/hicolor/*/apps/jabbim.png
%{_datadir}/icons/hicolor/scalable/apps/jabbim.svg
%{_datadir}/pixmaps/jabbim.png
%{_datadir}/pixmaps/jabbim.svg
%{jabbimdata}/

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# fill in the template for the starting script
sed -e 's|@JABBIMDATA@|%{jabbimdata}|g' %{SOURCE1} > jabbim

%build

%install
rm -rf %{buildroot}

desktop-file-install --vendor fedora \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    jabbim.desktop

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 jabbim %{buildroot}/%{_bindir}/jabbim
rm jabbim

# remove the files which are not useful for end-users
# and files which upstream forgot to remove
rm jabbim.sh jabbim.pro
rm images/32x32/status/rsvg2png.sh
rm widgets/preferences.py.orig

mkdir -p %{buildroot}/%{jabbimdata}
# take everything else upstream ships
cp -a . %{buildroot}/%{jabbimdata}

# these will be installed from their original location
rm %{buildroot}/%{jabbimdata}/{AUTHORS,COPYING}

for i in 16 22 32 48 ; do
    d="%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps"
    install -dm 755 "$d"
    install -m 644 -p images/${i}x${i}/apps/jabbim.png "$d/jabbim.png"
done

d="%{buildroot}%{_datadir}/icons/hicolor/scalable/apps"
install -dm 755 "$d"
install -m 644 -p images/scalable/apps/jabbim.svg "$d/jabbim.svg"

install -dm 755 %{buildroot}/%{_datadir}/pixmaps
pushd %{buildroot}/%{_datadir}/pixmaps
ln -s ../icons/hicolor/48x48/apps/jabbim.png .
ln -s ../icons/hicolor/scalable/apps/jabbim.svg .
popd

%clean
rm -rf %{buildroot}

