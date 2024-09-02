Name: IMSProg
Version: 1.4.3
Release: %autorelease

Summary: I2C, SPI and MicroWire EEPROM/Flash chip programmer for CH341a devices
Summary(ru_RU.UTF-8): I2C, SPI and MicroWire EEPROM/Flash программатор для CH341a устройств
License: GPL-3.0-or-later
Group: Devel

Url: https://github.com/bigbigmdm/%{name}
Source: https://github.com/bigbigmdm/%{name}/archive/refs/tags/v%{version}.tar.gz 

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
#BuildRequires: pkgconfig(qt5-linguist)
#BuildRequires: pkgconfig(qt5-qttools)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: cmake

%description
IMSProg - Linux IMSProg - I2C, SPI and MicroWire EEPROM/Flash chip programmer
for CH341a devices. The IMSProm is a free I2C EEPROM programmer tool for
CH341A device based on QhexEdit2 and modify SNANDer programmer.

This is a GUI program used widget QhexEditor. For setting the SPI chip
parameters you can use the Detect button for reading chip parameters
(JEDEC information reading) or manually setting it. The I2C and MicroWire
EEPROM only manually selected.

The chip database format is clone with EZP2019, EZP2020, EZP2023, Minpro I,
XP866+ programmers. You can edit the database use the EZP Chip data Editor.

%description -l ru_RU.UTF-8
IMSProg - Linux IMSProg - I2C, SPI and MicroWire EEPROM/Flash программатор
для CH341a устройств. IMSProm является бесплатной утилитой для
использования CH341A устройств в качестве программатора микросхем. Основана на
QhexEdit2 и модифицированном программаторе SNANDer.

Графический интерфейс программы использует виджеты QhexEditor. Для настройки
параметров чипа SPI вы можете использовать кнопку «Поиск» для чтения параметров
чипа (считывание информации JEDEC) или настроить его вручную. I2C и MicroWire
EEPROM выбираются только вручную.

Формат базы данных чипов клонируется программаторами EZP2019, EZP2020, EZP2023,
Minpro I, XP866+. Вы можете редактировать базу данных с помощью редактора данных
EZP Chip.

%prep

%autosetup -p1 -n %{name}-%{version}

# update translations
lrelease-qt5 IMSProg_editor/language/*.ts
lrelease-qt5 IMSProg_programmer/language/*.ts

%build
pushd IMSProg_editor
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build
popd

pushd IMSProg_programmer
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build
popd

%install
pushd IMSProg_editor
%cmake_install
popd

pushd IMSProg_programmer
%cmake_install
popd

# remove extra appdata
rm %buildroot%_datadir/metainfo/io.github.bigbigmdm.imsprog_database_update.metainfo.xml
rm %buildroot%_datadir/metainfo/io.github.bigbigmdm.imsprog_editor.metainfo.xml

# rename README
cp IMSProg_editor/README.md IMSProg_editor.md
cp IMSProg_programmer/README.md IMSProg_programmer.md

%files
%doc README.md IMSProg_editor.md IMSProg_programmer.md ChangeLog
%_docdir/imsprog/
%_bindir/IMSProg
%_bindir/IMSProg_editor
%_bindir/IMSProg_database_update
%_datadir/imsprog
%_datadir/applications/IMSProg.desktop
%_datadir/applications/IMSProg_editor.desktop
%_datadir/applications/IMSProg_database_update.desktop
%_datadir/metainfo/io.github.bigbigmdm.imsprog.metainfo.xml
/usr/lib/udev/rules.d/*.rules
%_datadir/pixmaps/chipEdit64.png
%_datadir/pixmaps/IMSProg64.png
%_datadir/pixmaps/IMSProg_database_update.png
/usr/share/man/man1/*.1.*

%changelog
* Wed Aug 21 2024 Mikhail Medvedev 1.4.3-1
- initial release

