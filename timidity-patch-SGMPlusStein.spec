#
# NOTE:
#
# 1. When big change is involved (e.g. timidity.cfg change location),
# so that new timidity binray and old patch RPM won't work together,
# increment this number by 1 for all timidity related RPMs
#
# 2. Current config is hand merged from freepats.cfg and crude.cfg,
# so if new version is available, please merge both config, and make
# sure all patch files listed in config file do exist.
#
%define patch_pkg_version 2

Name:		timidity-patch-SGMPlusStein
Version:	2.01
Release:	2
Summary:	Patch set for MIDI audio synthesis
Group:		Sound
License:	Public Domain
URL:		https://sites.google.com/site/soundfonts4u/
Source0:	SGM-V%{version}-JN5.2PlusStein.zip
BuildArch:	noarch
Provides:	timidity-instruments = %{patch_pkg_version}
Obsoletes:	timidity-instruments <= 1.0-19mdk
BuildRequires:	unzip

%description
A freely distributable set of soundfonts matching the General MIDI standard.

SGMv2.01-JN-SMPv1.1 is a high quality 262mb General Midi SoundFont.
Based on SGM-v2.01 (http://www.geocities.jp/shansoundfont/) with improved
quality acoustic guitars and customised pianos.

SGMv2.01-JNv5.2PlusStein as above a General Midi SoundFont but includes
also the high quality Steinway Piano. This is a large SoundFount being 618mb.
Best with devices with 2gb or more of ram.

%prep

%install
mkdir -p %{buildroot}%{_datadir}/timidity/SGMPlusStein
cd %{buildroot}%{_datadir}/timidity/SGMPlusStein/
unzip %{SOURCE0}

mkdir -p %{buildroot}%{_sysconfdir}/timidity
cat >%{buildroot}%{_sysconfdir}/timidity/timidity-SGMPlusStein.cfg <<EOF
dir %{_datadir}/timidity/SGMPlusStein

soundfont SGM-V%{version}-JN5.2PlusStein.sf2
EOF

%post
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-SGMPlusStein.cfg 25

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/update-alternatives --remove timidity.cfg %{_sysconfdir}/timidity/timidity-SGMPlusStein.cfg
fi

%triggerpostun -- TiMidity++ <= 2.13.2-1mdk
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-SGMPlusStein.cfg 25

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/timidity/timidity-SGMPlusStein.cfg
%{_datadir}/timidity/SGMPlusStein
