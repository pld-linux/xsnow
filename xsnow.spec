Summary:	Xsnow will spread Christmas cheer on your X display
Summary(de.UTF-8):   Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(es.UTF-8):   Para aquellos que desean una Navidad, los 12 meses del año
Summary(fr.UTF-8):   Xsnow va projeter l'esprit de noel sur votre écran X
Summary(pl.UTF-8):   Xsnow wprowadzi ekran X-ów w nastrój Bożego Narodzenia
Summary(pt_BR.UTF-8):   Para aqueles que desejam o Natal 12 meses por ano
Summary(tr.UTF-8):   X ekranına kar yağdırır
Name:		xsnow
Version:	1.42
Release:	2
License:	MIT
Group:		X11/Amusements
Source0:	http://www.euronet.nl/~rja/Xsnow/%{name}-%{version}.tar.gz
# Source0-md5:	451d8fc0a2b5393b428faa496a556036
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.xml
URL:		http://www.euronet.nl/~rja/Xsnow/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		xscreensaverdir	/etc/X11/xscreensaver

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l de.UTF-8
Umgeben von sanftem Schneegestöber fliegt Sankt Nikolaus in seinem
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee
gelegentlich von den Fenstern zu wischen!

%description -l es.UTF-8
Nieve cayendo continuamente acompañada por el vuelo de Papa Noel por
tu pantalla. ¡Y no te olvides sacudir las ventanas, de vez en cuando,
para quitar la nieve!

%description -l fr.UTF-8
Une douce chute de neige continue s'accompage du père Noël conduisant
son traineau à travers votre écran. N'oubliez pas de secouer la neige
de ces fenêtres de temps en temps !

%description -l pl.UTF-8
Pada śnieg, a Święty Mikołaj fruwa na swoich saniach po ekranie. Nie
zapomnij od czasu do czasu strząsnąć śnieg z okienek!

%description -l pt_BR.UTF-8
Neve caindo continuamente acompanhada pelo vôo do Papai Noel pela sua
tela. Não se esqueça de chacoalhar as janelas de vez em quando para
tirar a neve!

%description -l tr.UTF-8
Noel Baba'nın geyikleriyle birlikte karlar altında uçuşunu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini değiştirip
karları dağıtmayı unutmayın.

%prep
%setup -q

%build
xmkmf
%{__make} CCOPTIONS="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{xscreensaverdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{xscreensaverdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{xscreensaverdir}/*
