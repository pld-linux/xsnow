Summary:     Xsnow will spread Christmas cheer on your X display
Summary(de): Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(fr): Xsnow va projeter l'esprit de noel sur votre écran X.
Summary(pl): Xsnow wprowadzi ekran X-ów w nastrój Bo¿ego Narodzenia
Summary(tr): X ekranýna kar yaðdýrýr
Name:        xsnow
Version:     1.40
Release:     7
Copyright:   MIT
Group:       X11/Amusements
Source0:     ftp://ftp.x.org/contrib/games/%{name}-%{version}.tar.Z
Source1:     xsnow.wmconfig
BuildRoot:   /tmp/%{name}-%{version}-root

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l de
Umgeben von sanftem Schneegestöber fliegt Sankt Nikolaus in seinem 
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee 
gelegentlich von den Fenstern zu wischen! 

%description -l fr
Une douce chute de neige continue s'accompage du père Noël conduisant son
traineau à travers votre écran. N'oubliez pas de secouer la neige de ces
fenêtres de temps en temps !

%description -l pl
Pada ¶nieg, a ¦wiêty Miko³aj fruwa na swoich saniach po ekranie.
Nie zapomnij od czasu do czasu strz±sn±æ ¶nieg z okienek!

%description -l tr
Noel Baba'nýn geyikleriyle birlikte karlar altýnda uçuþunu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini deðiþtirip karlarý
daðýtmayý unutmayýn.

%prep
%setup -q

%build
xmkmf
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install install.man DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xsnow

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config %attr(644, root, root) /etc/X11/wmconfig/xsnow
%attr(755, root, root) /usr/X11R6/bin/xsnow
%attr(644, root,  man) /usr/X11R6/man/man1/xsnow.1x

%changelog
* Fri Sep 25 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.40-7]
- macro %%{name} in Source,
- macro %%{SOURCE1} in %install.

* Fri Sep 25 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
- added BuildRoot, allowing building from non-root account,
- added pl translation,
- `mkdir -p' replaced with more standard `install -d',
- added full %attr description in %files,
- use $RPM_OPT_FLAGS.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
