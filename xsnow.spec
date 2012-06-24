Summary:	Xsnow will spread Christmas cheer on your X display
Summary(de):	Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(es):	Para aquellos que desean una Navidad, los 12 meses del a�o
Summary(fr):	Xsnow va projeter l'esprit de noel sur votre �cran X
Summary(pl):	Xsnow wprowadzi ekran X-�w w nastr�j Bo�ego Narodzenia
Summary(pt_BR):	Para aqueles que desejam o Natal 12 meses por ano
Summary(tr):	X ekran�na kar ya�d�r�r
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
Icon:		xsnow.xpm
URL:		http://www.euronet.nl/~rja/Xsnow/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		xscreensaverdir	/etc/X11/xscreensaver

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l de
Umgeben von sanftem Schneegest�ber fliegt Sankt Nikolaus in seinem
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee
gelegentlich von den Fenstern zu wischen!

%description -l es
Nieve cayendo continuamente acompa�ada por el vuelo de Papa Noel por
tu pantalla. �Y no te olvides sacudir las ventanas, de vez en cuando,
para quitar la nieve!

%description -l fr
Une douce chute de neige continue s'accompage du p�re No�l conduisant
son traineau � travers votre �cran. N'oubliez pas de secouer la neige
de ces fen�tres de temps en temps !

%description -l pl
Pada �nieg, a �wi�ty Miko�aj fruwa na swoich saniach po ekranie. Nie
zapomnij od czasu do czasu strz�sn�� �nieg z okienek!

%description -l pt_BR
Neve caindo continuamente acompanhada pelo v�o do Papai Noel pela sua
tela. N�o se esque�a de chacoalhar as janelas de vez em quando para
tirar a neve!

%description -l tr
Noel Baba'n�n geyikleriyle birlikte karlar alt�nda u�u�unu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini de�i�tirip
karlar� da��tmay� unutmay�n.

%prep
%setup -q

%build
xmkmf
%{__make} CCOPTIONS="%{rpmcflags}" CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Amusements,%{_pixmapsdir},%{xscreensaverdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{xscreensaverdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_applnkdir}/Amusements/xsnow.desktop
%{_pixmapsdir}/*
%{xscreensaverdir}/*
