Summary:	Xsnow will spread Christmas cheer on your X display
Summary(de):	Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(fr):	Xsnow va projeter l'esprit de noel sur votre �cran X.
Summary(pl):	Xsnow wprowadzi ekran X-�w w nastr�j Bo�ego Narodzenia
Summary(tr):	X ekran�na kar ya�d�r�r
Name:		xsnow
Version:	1.40
Release:	10
Copyright:	MIT
Group:		X11/Amusements
Group(pl):	X11/Rozrywka
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tar.Z
Source1:	xsnow.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l de
Umgeben von sanftem Schneegest�ber fliegt Sankt Nikolaus in seinem
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee
gelegentlich von den Fenstern zu wischen!

%description -l fr
Une douce chute de neige continue s'accompage du p�re No�l conduisant
son traineau � travers votre �cran. N'oubliez pas de secouer la neige
de ces fen�tres de temps en temps !

%description -l pl
Pada �nieg, a �wi�ty Miko�aj fruwa na swoich saniach po ekranie. Nie
zapomnij od czasu do czasu strz�sn�� �nieg z okienek!

%description -l tr
Noel Baba'n�n geyikleriyle birlikte karlar alt�nda u�u�unu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini de�i�tirip
karlar� da��tmay� unutmay�n.

%prep
%setup -q

%build
xmkmf
%{__make} CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir} \
	install install.man 

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

%{_mandir}/man1/*
%{_applnkdir}/Amusements/xsnow.desktop
