Summary:	Xsnow will spread Christmas cheer on your X display
Summary(de):	Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(fr):	Xsnow va projeter l'esprit de noel sur votre écran X
Summary(pl):	Xsnow wprowadzi ekran X-ów w nastrój Bo¿ego Narodzenia
Summary(tr):	X ekranýna kar yaðdýrýr
Name:		xsnow
Version:	1.42
Release:	1
License:	MIT
Group:		X11/Amusements
Group(de):	X11/Unterhaltung
Group(pl):	X11/Rozrywka
Source0:	http://www.euronet.nl/~rja/Xsnow/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Icon:		xsnow.xpm
URL:		http://www.euronet.nl/~rja/Xsnow/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l de
Umgeben von sanftem Schneegestöber fliegt Sankt Nikolaus in seinem
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee
gelegentlich von den Fenstern zu wischen!

%description -l fr
Une douce chute de neige continue s'accompage du père Noël conduisant
son traineau à travers votre écran. N'oubliez pas de secouer la neige
de ces fenêtres de temps en temps !

%description -l pl
Pada ¶nieg, a ¦wiêty Miko³aj fruwa na swoich saniach po ekranie. Nie
zapomnij od czasu do czasu strz±sn±æ ¶nieg z okienek!

%description -l tr
Noel Baba'nýn geyikleriyle birlikte karlar altýnda uçuþunu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini deðiþtirip
karlarý daðýtmayý unutmayýn.

%prep
%setup -q

%build
xmkmf
%{__make} CCOPTIONS="%{rpmcflags}" CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Amusements,%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_applnkdir}/Amusements/xsnow.desktop
%{_pixmapsdir}/*
