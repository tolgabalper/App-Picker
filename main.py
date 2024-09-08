import platform
import subprocess

# '\x1B[1m' makes it bold.
# '\x1B[4m' makes it underlined.
# '\x1B[1;4m' makes it bold and underlined.
# \x1B[0m closing tag

plat = platform.system()

selection_cask = ["brew install --cask"]
selection_formula = ["brew install --formula"]

Choco_download = ["choco install"]

Scoop_part_1 = "scoop bucket add extras ; scoop bucket add games ; scoop bucket add versions ; scoop bucket add java ; scoop bucket add nonportable"
Scoop_part_2 = False
Scoop_download = ["scoop install"]

Winget_download = []

Apt_part_1 = "sudo add-apt-repository universe"
Apt_part_2 = False
Apt_download = ["sudo apt install -y"]

Flatpak_part_1 = "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo"
Flatpak_download = ["flatpak install flathub"]

Yay_download = ["yay -S"]

category_dic = {
    "1": "Browsers",
    "2": "Cloud",
    "3": "Compression",
    "4": "Creative",
    "5": "Dev Langs & Runtimes",
    "6": "Dev Tools",
    "7": "Documents",
    "8": "File Sharing",
    "9": "Gaming",
    "10": "Media",
    "11": "Communication",
    "12": "Security",
    "13": "Utility",
    "14": "Writing",
}

option = {
    "MacOS": {
        "Browsers": [
            ["Mozilla Firefox", "firefox", "cask"],
            ["Google Chrome", "google-chrome", "cask"],
            ["Chromium", "chromium", "cask"],
            ["Ungoogled Chromium", "eloston-chromium", "cask"],
            ["Arc", "arc", "cask"],
            ["Vivaldi", "vivaldi", "cask"],
            ["Opera", "opera", "cask"],
            ["Brave", "brave-browser", "cask"],
        ],
        "Cloud": [
            ["Dropbox", "dropbox", "cask"],
            ["Google Drive", "google-drive", "cask"],
            ["Insync", "insync", "cask"],
            ["Nextcloud", "nextcloud", "cask"],
            ["Syncthing (CLI)", "syncthing", "cask"],
        ],
        "Compression": [
            ["7-Zip", "sevenzip", "formula"],
        ],
        "Creative": [
            ["OBS Studio", "obs", "cask"],
            ["Audacity", "audacity", "cask"],
            ["Unity Hub", "unity", "cask"],
            ["Godot", "godot", "cask"],
            ["Godot (with Mono/C#)", "godot-mono", "cask"],
            ["Blender", "blender", "cask"],
            ["GIMP", "gimp", "cask"],
            ["Krita", "krita", "cask"],
            ["Figma", "figma", "cask"],
            ["Inkscape", "inkscape", "cask"],
        ],
        "Dev Langs & Runtimes": [
            ["Python 3", "python@3.11", "formula"],
            ["NodeJS", "node", "formula"],
            ["NodeJS (LTS)", "node@20", "formula"],
            ["Deno", "deno", "formula"],
            ["Oracle JDK 17", "oracle-jdk", "cask"],
            ["Open JDK 17", "openjdk@17", "formula"],
            ["Open JDK 21", "openjdk@21", "formula"],
            ["Go", "go", "formula"],
            ["Rust", "rust", "formula"],
            ["Rustup", "rustup-init", "formula"],
            ["Ruby", "ruby", "formula"],
            ["PHP", "php", "formula"],
            ["Perl", "perl", "formula"],
        ],
        "Dev Tools": [
            ["PowerShell", "powershell", "cask"],
            ["Visual Studio Code", "visual-studio-code", "cask"],
            ["VSCodium", "vscodium", "cask"],
            ["Git", "git", "formula"],
            ["Git LFS", "git-lfs", "formula"],
            ["AWS CLI", "awscli", "formula"],
            ["Azure CLI", "azure-cli", "formula"],
            ["Docker CLI", "docker", "formula"],
            ["Docker Desktop", "docker", "cask"],
            ["docker-compose", "docker-compose", "formula"],
            ["OpenSSH", "openssh", "formula"],
            ["PuTTY", "putty", "formula"],
            ["Arduino IDE", "arduino", "cask"],
            ["cURL", "curl", "formula"],
            ["GNU Wget", "wget", "formula"],
            ["VirtualBox", "virtualbox", "cask"],
            ["Wireshark (Formula)", "wireshark", "formula"],
            ["Wireshark (GUI)", "wireshark", "cask"],
        ],
        "Documents": [
            ["Foxit PDF Reader", "foxitreader", "cask"],
            ["Adobe Acrobat Reader", "adobe-acrobat-reader", "cask"],
        ],
        "File Sharing": [
            ["qBittorrent", "qbittorrent", "cask"],
            ["Transmission", "transmission", "cask"],
            ["Deluge", "deluge", "cask"],
        ],
        "Gaming": [
            ["Steam", "steam", "cask"],
            ["Epic Games Launcher", "epic-games", "cask"],
            ["GOG Galaxy", "gog-galaxy", "cask"],
            ["Heroic Games Launcher", "heroic", "cask"],
        ],
        "Media": [
            ["Spotify", "spotify", "cask"],
            ["VLC", "vlc", "cask"],
            ["foobar2000", "foobar2000", "cask"],
            ["Handbrake", "handbrake", "formula"],
            ["FFmpeg", "ffmpeg", "formula"],
        ],
        "Communication": [
            ["Discord", "discord", "cask"],
            ["Beeper", "beeper", "cask"],
            ["Slack", "slack", "cask"],
            ["Zoom", "zoom", "cask"],
            ["Skype", "skype", "cask"],
            ["Thunderbird", "thunderbird", "cask"],
        ],
        "Security": [
            ["Bitwarden", "bitwarden", "cask"],
            ["KeePassXC", "keepassxc", "cask"],
            ["QtPass", "qtpass", "cask"],
            ["LastPass", "lastpass", "cask"],
            ["OpenVPN", "openvpn", "formula"],
            ["Tailscale", "tailscale", "cask"],
            ["WireGuard", "wireguard-tools", "formula"],
        ],
        "Utility": [
            ["Etcher", "balenaetcher", "cask"],
            ["Flameshot", "flameshot", "cask"],
        ],
        "Writing": [
            ["Notion", "notion", "cask"],
            ["Obsidian", "obsidian", "cask"],
            ["Logseq", "logseq", "cask"],
            ["LibreOffice", "libreoffice", "cask"],
        ],
    },
    "Windows": {
        "Choco": {
            "Browsers": [
                ["Nozilla Firefox", "firefox"],
                ["Google Chrome", "googlechrome"],
                ["Chromium", "chromium"],
                ["Ungoogled Chromium", "ungoogled-chromium"],
                ["Vivaldi", "vivaldi"],
                ["Opera", "opera"],
                ["Brave", "brave"],
            ],
            "Cloud": [
                ["Dropbox", "dropbox"],
                ["Google Drive", "googledrive"],
                ["Insync", "insync"],
                ["Nextcloud", "nextcloud-client"],
                ["Syncthing (CLI)", "syncthing"],
            ],
            "Compression": [
                ["7-Zip", "7zip"],
                ["PeaZip", "peazip.install"],
                ["WinRAR", "winrar"],
            ],
            "Creative": [
                ["OBS Studio", "obs-studio"],
                ["Audacity", "audacity"],
                ["Unity Hub", "unity-hub"],
                ["Godot", "godot"],
                ["Godot (with Mono/C#)", "godot-mono"],
                ["Blender", "blender"],
                ["Paint.NET", "paint.net"],
                ["GIMP", "gimp"],
                ["Krita", "krita"],
                ["Figma", "figma"],
                ["Inkscape", "inkscape"],
            ],
            "Dev Langs & Runtimes": [
                ["Python 3", "python"],
                ["Python 2", "python2"],
                ["NodeJS", "nodejs.install"],
                ["NodeJS (LTS)", "nodejs-lts"],
                ["nvm (Node Version Manager)", "nvm"],
                ["Deno", "deno"],
                ["Oracle JDK 21", "oracalejdk"],
                ["Oracle JDK 17", "oraclejdk17"],
                ["Go", "golang"],
                ["Rust", "rust"],
                ["Rust MSVC", "rust-ms"],
                ["Rustup", "rustup.install"],
                ["Ruby", "ruby"],
                ["PHP", "php"],
                ["Perl", "strawberryperl"],
            ],
            "Dev Tools": [
                ["PowerShell", "powershell"],
                ["Visual Studio Code", "vscode"],
                ["VSCodium", "vscodium"],
                ["Notepad++", "notepadplusplus.install"],
                ["Git", "git"],
                ["Git LFS", "git-lfs"],
                ["AWS CLI", "awscli"],
                [
                    "Azure CLI",
                ],
            ],
            "Documents": [
                ["Foxit PDF Reader", "foxitreader"],
                ["Sumatra PDF Reader", "sumatrapdf"],
                ["Adobe Acrobat Reader", "adobereader"],
                ["PDFCreator", "pdfcreator"],
                ["CutePDF", "cutepdf"],
            ],
            "File Sharing": [
                ["qBittorrent", "qbittorrent"],
                ["Transmission", "transmission"],
                ["Deluge", "deluge"],
            ],
            "Gaming": [
                ["Steam", "steam"],
                ["Epic Games Launcher", "epicgameslauncher"],
                ["GOG Galaxy", "goggalaxy"],
                ["Legendary CLI Games Launcher", "legendary"],
            ],
            "Media": [
                ["Spotify", "spotify"],
                ["iTunes", "itunes"],
                ["VLC", "vlc"],
                ["foobar2000", "foobar2000"],
                ["MPC-HC", "mpc-hc"],
                ["K-Lite Codec Pack (Full)", "k-litecodecpackfull"],
                ["Handbrake", "handbrake"],
                ["FFmpeg", "ffmpeg"],
            ],
            "Communication": [
                ["Discord", "discord.install"],
                ["Slack", "slack"],
                ["Zoom", "zoom"],
                ["Skype", "skype"],
                ["Thunderbird", "thunderbird"],
            ],
            "Security": [
                ["Bitwarden", "bitwarden"],
                ["KeePassXC", "keepassxc"],
                ["Keepass", "keepass"],
                ["QtPass", "qtpass"],
                ["LastPass", "lastpass"],
                ["OpenVPN", "openvpn"],
                ["Tailscale", "tailscale"],
                ["WireGuard", "wireguard"],
            ],
            "Utility": [
                ["PowerToys", "powertoys"],
                ["Everything", "everything"],
                ["TeraCopy", "teracopy"],
                ["TreeSize Free", "treesizefree"],
                ["CPU-Z", "cpu-z.install"],
                ["GPU-Z", "gpu-z.portable"],
                ["Etcher", "etcher"],
                ["Rufus", "rufus"],
                ["AutoHotkey", "autohotkey"],
                ["Sysinternals Suite", "sysinternals"],
                ["Lightshot", "lightshot.install"],
                ["Flameshot", "flameshot"],
            ],
            "Writing": [
                ["Notion", "notion"],
                ["Obsidian", "obsidian"],
                ["Logseq", "logseq"],
                ["LibreOffice", "libreoffice-fresh"],
            ],
        },
        "Scoop": {
            "Browsers": [
                ["Mozilla Firefox", "extras/firefox"],
                ["Google Chrome", "extras/googlechrome"],
                ["Chromium", "extras/chromium"],
                ["Ungoogled Chromium", "extras/ungoogled-chromium"],
                ["Vivaldi", "extras/vivaldi"],
                ["Opera", "extras/opera"],
                ["Brave", "extras/brave"],
            ],
            "Cloud": [
                ["Dropbox", "nonportable/dropbox-np"],
                ["Nextcloud", "extras/nextcloud"],
                ["Syncthing (CLI)", "main/syncthing"],
            ],
            "Compression": [
                ["7-Zip", "main/7zip"],
                ["PeaZip", "extras/peazip"],
                ["WinRAR", "nonportable/winrar-np"],
            ],
            "Creative": [
                ["OBS Studio", "extras/obs-studio"],
                ["Audacity", "extras/audacity"],
                ["Unity Hub", "nonportable/unity-hub-np"],
                ["Godot", "extras/godot"],
                ["Godot (with Mono/C#)", "extras/godot-mono"],
                ["Blender", "extras/blender"],
                ["Paint.NET", "extras/paint.net"],
                ["GIMP", "extras/gimp"],
                ["Krita", "extras/krita"],
                ["Figma", "extras/figma"],
                ["Inkscape", "extras/inkscape"],
            ],
            "Dev Langs & Runtimes": [
                ["Python 3", "versions/python311"],
                ["Python2", "versions/python27"],
                ["NodeJS", "main/nodejs"],
                ["NodeJS (LTS)", "main/nodejs-lts"],
                ["nvm (Node Version Manager)", "main/nvm"],
                ["Deno", "main/deno"],
                ["Oracle JDK 21", "java/oraclejdk-lts"],
                ["Open JDK 17", "java/openjdk17"],
                ["Open JDK 21", "java/openjdk21"],
                ["Go", "main/go"],
                ["Rust", "main/rust"],
                ["Rust MSVC", "main/rust-msvc"],
                ["Rustup", "main/rustup"],
                ["Ruby", "main/ruby"],
                ["PHP", "main/php"],
                ["Perl", "main/perl"],
            ],
            "Dev Tools": [
                ["Visual Studio Code", "extras/vscode"],
                ["VSCodium", "extras/vscodium"],
                ["Notepad++", "extras/notepadplusplus"],
                ["Git", "main/git"],
                ["Git LFS", "main/git-lfs"],
                ["AWS CLI", "main/aws"],
                ["Azure CLI", "main/azure-cli"],
                ["Docker CLI", "main/docker"],
                ["docker-compose", "main/docker-compose"],
                ["OpenSSH", "main/openssh"],
                ["WinSCP", "extras/winscp"],
                ["FileZilla", "extras/filezilla"],
                ["PuTTY", "extras/putty"],
                ["Arduino IDE", "extras/arduino"],
                ["cURL", "main/curl"],
                ["GNU Wget", "main/wget"],
                ["VirtualBox", "nonportable/virtualbox-np"],
                ["Wireshark", "extras/wireshark"],
                ["OpenSSH", "openssh"],
                ["WinSCP", "winscp"],
                ["FileZilla", "filezilla"],
                ["PuTTY", "putty"],
                ["Arduino IDE", "arduino"],
                ["cURL", "curl"],
                ["GNU Wget", "wget"],
                ["VirtualBox", "virtualbox"],
                ["Wireshark", "wireshark"],
            ],
            "Documents": [
                ["Foxit PDF Reader", "extras/foxit-pdf-reader"],
                ["Sumatra PDF Reader", "extras/sumatrapdf"],
            ],
            "File Sharing": [
                ["qBittorrent", "extras/qbittorrent"],
                ["Transmission", "extras/transmission"],
                ["Deluge", "extras/deluge"],
            ],
            "Gaming": [
                ["Steam", "versions/steam"],
                ["Epic Games Launcher", "epic-games-launcher"],
                ["GOG Galaxy", "games/goggalaxy"],
                ["Heroic Games Launcher", "games/heroic-games-launcher"],
            ],
            "Media": [
                ["Spotify", "extras/spotify"],
                ["VLC", "extras/vlc"],
                ["foobar2000", "extras/foobar2000"],
                ["MPC-HC", "extras/mpc-hc"],
                ["K-Lite Codec Pack (Full)", "nonportable/k-lite-codec-pack-full-np"],
                ["Handbrake", "extras/handbrake"],
                ["FFmpeg", "main/ffmpeg"],
            ],
            "Communication": [
                ["Discord", "extras/discord"],
                ["Slack", "extras/slack"],
                ["Zoom", "extras/zoom"],
                ["Skype", "extras/skype"],
                ["Thunderbird", "extras/thunderbird"],
            ],
            "Security": [
                ["Bitwarden", "extras/bitwarden"],
                ["KeePassXC", "extras/keepassxc"],
                ["Keepass", "extras/keepass"],
                ["OpenVPN", "extras/openvpn"],
                ["Tailscale", "extras/tailscale"],
                ["WireGuard", "nonportable/wireguard-np"],
            ],
            "Utility": [
                ["PowerToys", "nonportable/powertoys-np"],
                ["Everything", "nonportable/everything-np"],
                ["TeraCopy", "nonportable/teracopy-np"],
                ["TreeSize Free", "extras/treesize-free"],
                ["CPU-Z", "extras/cpu-z"],
                ["GPU-Z", "extras/gpu-z"],
                ["Etcher", "extras/etcher"],
                ["Rufus", "extras/rufus"],
                ["AutoHotkey", "extras/autohotkey"],
                ["Sysinternals Suite", "extras/sysinternals"],
                ["Lightshot", "versions/lightshot"],
                ["Flameshot", "extras/flameshot"],
            ],
            "Writing": [
                ["Notion", "extras/notion"],
                ["Obsidian", "extras/obsidian"],
                ["Logseq", "extras/logseq"],
                ["LibreOffice", "extras/libreoffice"],
            ],
        },
        "Winget": {
            "Browsers": [
                ["Mozilla Firefox", "Mozilla.Firefox"],
                ["Google Chrome", "Google.Chrome"],
                ["Chromium", "Hibbiki.Chromium"],
                ["Ungoogled Chromium", "eloston.ungoogled-chromium"],
                ["Vivaldi", "VivaldiTechnologies.Vivaldi"],
                ["Opera", "Opera.Opera"],
                ["Brave", "Brave.Brave"],
            ],
            "Cloud": [
                ["Dropbox", "Dropbox.Dropbox"],
                ["Google Drive", "Google.Drive"],
                ["Insync", "Insynchq.Insync"],
                ["Nextcloud", "Nextcloud.NextcloudDesktop"],
            ],
            "Compression": [
                ["7-Zip", "7zip.7zip"],
                ["PeaZip", "Giorgiotani.Peazip"],
                ["WinRAR", "RARLab.WinRAR"],
            ],
            "Creative": [
                ["OBS Studio", "OBSProject.OBSStudio"],
                ["Audacity", "Audacity.Audacity"],
                ["Unity Hub", "Unity.UnityHub"],
                ["Godot", "GodotEngine.GodotEngine"],
                ["Godot (with Mono/C#)", "GodotEngine.GodotEngine.Mono"],
                ["Blender", "BlenderFoundation.Blender"],
                ["Paint.NET", "dotPDNLLC.paintdotnet"],
                ["GIMP", "gimp.gimp"],
                ["Figma", "Figma.Figma"],
                ["Inkscape", "Inkscape.Inkscape"],
            ],
            "Dev Langs & Runtimes": [
                ["Python 3", "Python.Python.3.11"],
                ["Python2", "Python.Python -v 2"],
                ["NodeJS", "OpenJS.Nodejs"],
                ["NodeJS (LTS)", "OpenJS.NodeJS.LTS"],
                ["Deno", "DenoLand.Deno"],
                ["Oracle JDK 17", "Oracle.JDK.17"],
                ["Go", "GoLang.Go.1.19"],
                ["Rust MSVC", "Rustlang.Rust.MSVC"],
                ["Rustup", "Rustlang.Rustup"],
                ["Ruby", "RubyInstallerTeam.RubyWithDevKit"],
                ["Perl", "StrawberryPerl.StrawberryPerl"],
            ],
            "Dev Tools": [
                ["PowerShell", "Microsoft.Powershell"],
                ["Visual Studio Code", "Microsoft.VisualStudioCode"],
                ["VSCodium", "VSCodium.VSCodium"],
                ["Notepad++", "Notepad++.Notepad++"],
                ["Git", "Git.Git"],
                ["Git LFS", "GitHub.GitLFS"],
                ["AWS CLI", "Amazon.AWSCLI"],
                ["Azure CLI", "Microsoft.AzureCLI"],
                ["Docker Desktop", "Docker.DockerDesktop"],
                ["OpenSSH", "Microsoft.OpenSSH.Beta"],
                ["WinSCP", "WinSCP.WinSCP"],
                ["FileZilla", "TimKosse.FilezillaClient"],
                ["PuTTY", "PuTTY.PuTTY"],
                ["Arduino IDE", "ArduinoSA.IDE.stable"],
                ["GNU Wget", "JernejSimoncic.Wget"],
                ["VirtualBox", "Oracle.VirtualBox"],
                ["Wireshark", "WiresharkFoundation.Wireshark"],
            ],
            "Documents": [
                ["Foxit PDF Reader", "Foxit.FoxitReader"],
                ["Sumatra PDF Reader", "SumatraPDF.SumatraPDF"],
                ["Adobe Acrobat Reader", "Adobe.Acrobat.Reader.64-bit"],
                ["PDFCreator", "pdfforge.PDFCreator"],
                ["CutePDF", "AcroSoftwareInc.CutePDFWriter"],
            ],
            "File Sharing": [
                ["qBittorrent", "qBittorrent.qBittorrent"],
            ],
            "Gaming": [
                ["Steam", "Valve.Steam"],
                ["Epic Games Launcher", "EpicGames.EpicGamesLauncher"],
                ["GOG Galaxy", "GOG.Galaxy"],
                ["Heroic Games Launcher", "HeroicGamesLauncher.HeroicGamesLauncher"],
            ],
            "Media": [
                ["Spotify", "Spotify.Spotify"],
                ["iTunes", "Apple.iTunes"],
                ["VLC", "Videolan.Vlc"],
                ["foobar2000", "PeterPawlowski.foobar2000"],
                ["MPC-HC", "clsid2.mpc-hc"],
                ["K-Lite Codec Pack (Full)", "CodecGuide.K-LiteCodecPack.Full"],
                ["Handbrake", "HandBrake.HandBrake"],
            ],
            "Communication": [
                ["Discord", "Discord.Discord"],
                ["Beeper", "NovaTechnology.Beeper"],
                ["Slack", "SlackTechnologies.Slack"],
                ["Zoom", "Zoom.Zoom"],
                ["Skype", "Microsoft.Skype"],
                ["Thunderbird", "Mozilla.Thunderbird"],
            ],
            "Security": [
                ["Bitwarden", "Bitwarden.Bitwarden"],
                ["KeePassXC", "KeePassXCTeam.KeePassXC"],
                ["Keepass", "DominikReichl.KeePass"],
                ["QtPass", "IJHack.QtPass"],
                ["LastPass", "LogMeIn.LastPass"],
                ["OpenVPN", "OpenVPNTechnologies.OpenVPN"],
                ["Tailscale", "tailscale.tailscale"],
                ["WireGuard", "WireGuard.WireGuard"],
            ],
            "Utility": [
                ["PowerToys", "Microsoft.PowerToys"],
                ["Everything", "voidtools.Everything"],
                ["TeraCopy", "CodeSector.TeraCopy"],
                ["TreeSize Free", "JAMSoftware.TreeSize"],
                ["CPU-Z", "CPUID.CPU-Z"],
                ["GPU-Z", "TechPowerUp.GPU-Z"],
                ["Etcher", "Balena.Etcher"],
                ["Rufus", "Rufus.Rufus"],
                ["AutoHotkey", "Lexikos.AutoHotkey"],
                ["Lightshot", "Skillbrains.Lightshot"],
                ["Flameshot", "Flameshot.Flameshot"],
            ],
            "Writing": [
                ["Notion", "Notion.Notion"],
                ["Obsidian", "Obsidian.Obsidian"],
                ["Logseq", "Logseq.Logseq"],
                ["LibreOffice", "LibreOffice.LibreOffice"],
            ],
        },
    },
    "Linux": {
        "Apt": {
            "Browsers": [
                ["Mozilla Firefox", "firefox"],
                ["Chromium", "chromium-browser"],
            ],
            "Compression": [
                ["7-Zip", "7zip"],
            ],
            "Creative": [
                ["LAME for Audacity", "lame"],
            ],
            "Dev Langs & Runtimes": [
                ["Python 3", "python3"],
                ["Python2", "python2"],
                ["Open JDK 17", "openjdk-17-jdk"],
                ["Go", "golang"],
                ["Rust", "rust-all"],
                ["Ruby", "ruby"],
                ["PHP", "php"],
                ["Perl", "perl"],
            ],
            "Dev Tools": [
                ["Git", "git"],
                ["Git LFS", "git-lfs"],
                ["AWS CLI", "awscli"],
                ["Docker Desktop", "docker"],
                ["docker-compose", "docker-compose"],
                ["FileZilla", "filezilla"],
                ["PuTTY", "putty"],
                ["Arduino IDE", "arduino-ide"],
                ["cURL", "curl"],
                ["GNU Wget", "wget"],
                ["VirtualBox", "virtualbox"],
                ["Wireshark", "wireshark"],
            ],
            "Gaming": [
                ["Steam", "steam"],
                ["Lutris", "lutris"],
            ],
            "Media": [
                ["VLC", "vlc"],
                ["Handbrake", "handbrake"],
                ["FFmpeg", "ffmpeg"],
            ],
            "Communication": [
                ["Thunderbird", "thunderbird"],
            ],
            "Security": [
                ["KeePassXC", "keepassxc"],
                ["QtPass", "qtpass"],
                ["OpenVPN", "openvpn"],
                ["WireGuard", "wireguard"],
            ],
            "Utility": [
                ["Flameshot", "flameshot"],
            ],
            "Writing": [
                ["LibreOffice", "libreoffice"],
            ],
        },
        "Flatpak": {
            "Browsers": [
                ["Mozilla Firefox", "org.mozilla.firefox"],
                ["Google Chrome", "com.google.Chrome"],
                ["Chromium", "org.chromium.Chromium"],
                [
                    "Ungoogled Chromium",
                    "io.github.ungoogled_software.ungoogled_chromium",
                ],
                ["Vivaldi", "com.vivaldi.Vivaldi"],
                ["Opera", "com.opera.Opera"],
                ["Brave", "com.brave.Browser"],
            ],
            "Cloud": [
                ["Dropbox", "com.dropbox.Client"],
                ["Nextcloud", "com.nextcloud.desktopclient.nextcloud"],
            ],
            "Compression": [
                ["PeaZip", "io.github.peazip.PeaZip"],
            ],
            "Creative": [
                ["OBS Studio", "com.obsproject.Studio"],
                ["Audacity", "org.audacityteam.Audacity"],
                ["Unity Hub", "com.unity.UnityHub"],
                ["Godot", "org.godotengine.Godot"],
                ["Blender", "org.blender.Blender"],
                ["GIMP", "org.gimp.GIMP"],
                ["Krita", "org.kde.krita"],
                ["Figma", "io.github.Figma_Linux.figma_linux"],
                ["Inkscape", "org.inkscape.Inkscape"],
            ],
            "Dev Tools": [
                ["Visual Studio Code", "com.visualstudio.code"],
                ["VSCodium", "com.vscodium.codium"],
                ["FileZilla", "org.filezillaproject.Filezilla"],
                ["PuTTY", "uk.org.greenend.chiark.sgtatham.putty"],
                ["Arduino IDE", "cc.arduino.IDE2"],
                ["Wireshark", "org.wireshark.Wireshark"],
            ],
            "File Sharing": [
                ["qBittorrent", "org.qbittorrent.qBittorrent"],
                ["Transmission", "com.transmissionbt.Transmission"],
                ["Deluge", "org.deluge_torrent.deluge"],
            ],
            "Gaming": [
                ["Steam", "com.valvesoftware.Steam"],
                ["Heroic Games Launcher", "com.heroicgameslauncher.hgl"],
                ["Lutris", "net.lutris.Lutris"],
            ],
            "Media": [
                ["Spotify", "com.spotify.Client"],
                ["VLC", "org.videolan.VLC"],
                ["Handbrake", "fr.handbrake.ghb"],
            ],
            "Communication": [
                ["Discord", "com.discordapp.Discord"],
                ["Slack", "com.slack.Slack"],
                ["Zoom", "us.zoom.Zoom"],
                ["Skype", "com.skype.Client"],
                ["Thunderbird", "org.mozilla.Thunderbird"],
            ],
            "Security": [
                ["Bitwarden", "com.bitwarden.desktop"],
                ["KeePassXC", "org.keepassxc.KeePassXC"],
                ["Keepass", "org.keepassxc.KeePassXC"],
            ],
            "Utility": [
                ["Flameshot", "org.flameshot.Flameshot"],
            ],
            "Writing": [
                ["Obsidian", "md.obsidian.Obsidian"],
                ["Logseq", "com.logseq.Logseq"],
                ["LibreOffice", "org.libreoffice.LibreOffice"],
            ],
        },
        "Yay": {
            "Browsers": [
                ["Mozilla Firefox", "firefox"],
                ["Google Chrome", "google-chrome"],
                ["Chromium", "chromium"],
                ["Ungoogled Chromium", "ungoogled-chromium-bin"],
                ["Vivaldi", "vivaldi"],
                ["Opera", "opera"],
                ["Brave", "brave-bin"],
            ],
            "Cloud": [
                ["Dropbox", "dropbox"],
                ["Insync", "insync"],
                ["Nextcloud", "nextcloud"],
                ["Syncthing (CLI)", "syncthing"],
            ],
            "Compression": [
                ["7-Zip", "7-zip-full"],
                ["PeaZip", "peazip-qt-bin"],
            ],
            "Creative": [
                ["OBS Studio", "obs-studio"],
                ["LAME for Audacity", "lame"],
                ["Unreal Engine", "unreal-engine"],
                ["Godot", "godot"],
                ["Godot (with Mono/C#)", "godot-mono-bin"],
            ],
            "Dev Langs & Runtimes": [
                ["Python 3", "python"],
                ["Python2", "python2"],
                ["NodeJS", "nodejs"],
                ["NodeJS (LTS)", "nodejs-lts-iron"],
                ["Deno", "deno"],
                ["Oracle JDK 17", "jdk-lts"],
                ["Open JDK 17", "jre17-openjdk"],
                ["Open JDK 21", "jdk-openjdk"],
                ["Go", "go"],
                ["Rust", "rust"],
                ["Rustup", "rustup"],
                ["Ruby", "ruby"],
                ["PHP", "php"],
                ["Perl", "perl"],
            ],
            "Dev Tools": [
                ["PowerShell", "powershell-bin"],
                ["Visual Studio Code", "visual-studio-code-bin"],
                ["VSCodium", "vscodium-bin"],
                ["Git", "git"],
                ["Git LFS", "git-lfs"],
                ["AWS CLI", "aws-cli"],
                ["Azure CLI", "azure-cli"],
                ["Docker Desktop", "docker"],
                ["docker-compose", "docker-compose"],
                ["OpenSSH", "openssh"],
                ["FileZilla", "filezilla"],
                ["PuTTY", "putty"],
                ["Arduino IDE", "arduino-ide"],
                ["cURL", "curl"],
                ["GNU Wget", "wget"],
                ["VirtualBox", "virtualbox"],
                ["Wireshark", "wireshark-qt"],
            ],
            "Documents": [
                ["Foxit PDF Reader", "foxitreader"],
            ],
            "Gaming": [
                ["Steam", "steam"],
                ["Heroic Games Launcher", "heroic-games-launcher-bin"],
                ["Legendary CLI Games Launcher", "legendary"],
                ["Lutris", "lutris"],
            ],
            "Media": [
                ["Spotify", "spotify"],
                ["VLC", "vlc"],
                ["foobar2000", "foobar2000"],
                ["Handbrake", "handbrake"],
                ["FFmpeg", "ffmpeg"],
            ],
            "Communication": [
                ["Discord", "discord"],
                ["Beeper", "beeper-latest-bin"],
                ["Slack", "slack-desktop"],
                ["Zoom", "zoom"],
                ["Skype", "skypeforlinux-stable-bin"],
                ["Thunderbird", "thunderbird"],
            ],
            "Security": [
                ["Bitwarden", "bitwarden"],
                ["KeePassXC", "keepassxc"],
                ["QtPass", "qtpass"],
                ["LastPass", "lastpass"],
                ["OpenVPN", "openvpn"],
                ["Tailscale", "tailscale"],
                ["WireGuard", "wireguard-tools"],
            ],
            "Utility": [
                ["Etcher", "etcher-bin"],
                ["Flameshot", "flameshot"],
            ],
            "Writing": [
                ["Notion", "notion-app-electron"],
                ["Obsidian", "obsidian-bin"],
                ["Logseq", "logseq-desktop-bin"],
                ["LibreOffice", "libreoffice-fresh"],
            ],
        },
    },
}


def search(os, package_manager, category2):
    global Apt_part_2, Scoop_part_2
    if os == "windows":
        if package_manager == "choco":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    return Choco_download.append(
                        option[os.capitalize()][package_manager.capitalize()][
                            category_dic[category2]
                        ][int(choice) - 1][1]
                    )
                elif choice.__contains__("desc:"):
                    choice = choice.removeprefix("desc:")
                    subprocess.call(
                        "choco info {0}".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
        elif package_manager == "scoop":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    return Scoop_download.append(
                        option[os.capitalize()][package_manager.capitalize()][
                            category_dic[category2]
                        ][int(choice) - 1][1]
                    )
                elif choice.__contains__("desc:") and not Scoop_part_2:
                    choice = choice.removeprefix("desc:")
                    subprocess.call(Scoop_part_1, shell=True)
                    Scoop_part_2 = True
                    subprocess.call(
                        "scoop info {0} -v".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice.__contains__("desc:") and Scoop_part_2:
                    choice = choice.removeprefix("desc:")
                    subprocess.call(
                        "scoop info {0} -v".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
        elif package_manager == "winget":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    choice = "winget install -e --id {0} ".format(
                        option[os.capitalize()][package_manager.capitalize()][
                            category_dic[category2]
                        ][int(choice) - 1][1]
                    )
                    return Winget_download.append(choice)
                elif choice.__contains__("desc:"):
                    choice = choice.removeprefix("desc:")
                    subprocess.call(
                        "winget show -e --id {0}".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
    elif os == "linux":
        if package_manager == "apt":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    return Apt_download.append(
                        option[os.capitalize()][package_manager.capitalize()][
                            category_dic[category2]
                        ][int(choice) - 1][1]
                    )
                elif choice.__contains__("desc:") and not Apt_part_2:
                    choice = choice.removeprefix("desc:")
                    subprocess.call(Apt_part_1, shell=True)
                    Apt_part_2 = True
                    subprocess.call(
                        "apt info {0}".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice.__contains__("desc:") and Apt_part_2:
                    choice = choice.removeprefix("desc:")
                    subprocess.call(
                        "apt info {0}".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
        elif package_manager == "flatpak":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    return Flatpak_download.append(
                        option[os.capitalize()][package_manager.capitalize()][
                            category_dic[category2]
                        ][int(choice) - 1][1]
                    )
                elif choice.__contains__("desc:"):
                    choice = choice.removeprefix("desc:")
                    subprocess.call(Flatpak_part_1, shell=True)
                    subprocess.call(
                        "flatpak remote-info flathub {0}".format(
                            option[os.capitalize()][package_manager.capitalize()][
                                category_dic[category2]
                            ][int(choice) - 1][1]
                        ),
                        shell=True,
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
        elif package_manager == "yay":
            while True:
                print("\x1B[2J")
                counter = 1
                for sublist in option[os.capitalize()][package_manager.capitalize()][
                    category_dic[category2]
                ]:
                    application_name = sublist[0]
                    application_name = application_name.capitalize()
                    print(f"({counter}) {application_name}" + "\n", sep="\n")
                    counter += 1
                print(
                    """
        If you want to view details about a program type "desc:{ corresponding number }"

        If you want to select a program type "{ Corresponding number }"

        Press enter to return back to main menu
                    """
                )
                choice = input("Enter the corresponding number...")
                if not choice.__contains__("desc:") and not choice == "":
                    choice = option["Linux"]["Winget"][category_dic[category2]][
                        int(choice) - 1
                    ][1]
                    return Yay_download.append(choice)
                elif choice.__contains__("desc:"):
                    print(
                        "I could not find any information about how to view details about a program in Yay"
                    )
                    print(
                        "Because of that this feature is not available for this package manager"
                    )
                    choice = input("To return back press enter...")
                elif choice == "":
                    category2 = ""
                    break
    elif os == "MacOS":
        while True:
            print("\x1B[2J")
            counter = 1
            for sublist in option[os][category_dic[category2]]:
                application_name = sublist[0]
                application_name = application_name.capitalize()
                print(f"({counter}) {application_name}" + "\n", sep="\n")
                counter += 1
            print(
                """
    If you want to view details about a program type "desc:{ corresponding number }"

    If you want to select a program type "{ Corresponding number }"

    Press enter to return back to main menu
                """
            )
            choice = input("Enter the corresponding number...")
            if not choice.__contains__("desc:") and not choice == "":
                cask_check = option[os][category_dic[category2]][int(choice) - 1][2]
                if cask_check == "cask":
                    return selection_cask.append(
                        option[os][category_dic[category2]][int(choice) - 1][1]
                    )
                elif cask_check == "formula":
                    selection_formula.append(
                        option[os][category_dic[category2]][int(choice) - 1][1]
                    )
            elif choice.__contains__("desc:"):
                choice = choice.removeprefix("desc:")
                cask_check = option[os][category_dic[category2]][int(choice) - 1][2]
                choice = option[os][category_dic[category2]][int(choice) - 1][1]
                subprocess.call(
                    "brew info --{0} {1}".format(cask_check, choice), shell=True
                )
                choice = input("To return back press enter...")
            elif choice == "":
                category2 = ""
                break


print("Welcome to sys-configurator")
input("Press Enter to continue...")
print("\x1B[2J")

if plat == "Windows":
    os_list = list(option[plat].keys())
    for i in range(len(os_list)):
        print(f"({i + 1}) {os_list[i]} \n")

    print(
        "Please note that if it is not first time you are logging in to Windows, Winget must be installed \n"
    )
    source = input("Please select your preferred Source...")

    if source == "1" or source.capitalize() == os_list[0]:
        isChocolateyinstalled = input("Is Chocolatey installed? Y/n... ")
        while True:
            if (
                isChocolateyinstalled.lower() == "y"
                or isChocolateyinstalled.lower() == "yes"
                or isChocolateyinstalled == ""
            ):
                print("\x1B[2J")
                print("These are the options \n")
                for i in category_dic.items():
                    print(i, sep="\n")
                print("To start downloading procedure type download")
                category = input(
                    "Enter the corresponding number of the category you want to see..."
                )
                if category != "download" and int(category) in range(
                    1, len(category_dic)
                ):
                    search("windows", "choco", category)
                elif category.lower() == "download" and len(Choco_download) > 1:
                    Choco_download = " ".join(Choco_download)
                    print(Choco_download, sep="\n")
                    subprocess.call(Choco_download, shell=True)
            elif isChocolateyinstalled.lower() == "n" or isChocolateyinstalled == "no":
                print("\n Installing Chocolatey (https://chocolatey.org/) \n")
                subprocess.call(
                    "Set - ExecutionPolicy Bypass -Scope Process -Force; iex ((New - Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
                )
                print("\x1B[2J")
                isChocolateyinstalled = "y"
                break
    elif source == "2" or source.capitalize() == os_list[1]:
        isScoopinstalled = input("Is Scoop installed? Y/n... ")
        while True:
            if (
                isScoopinstalled.lower() == "y"
                or isScoopinstalled.lower() == "yes"
                or isScoopinstalled == ""
            ):
                print("\x1B[2J")
                print("These are the options \n")
                for i in category_dic.items():
                    print(i, sep="\n")
                print("To start downloading procedure type download")
                category = input(
                    "Enter the corresponding number of the category you want to see..."
                )
                if category != "download" and int(category) in range(
                    1, len(category_dic)
                ):
                    search("windows", "scoop", category)
                elif (
                    category.lower() == "download"
                    and len(Scoop_download) > 1
                    and not Scoop_part_2
                ):
                    subprocess.call(Scoop_part_1, shell=True)
                    Scoop_download = " ".join(Scoop_download)
                    print(Scoop_download, sep="\n")
                    subprocess.call(Scoop_download, shell=True)
                    exit()
                elif (
                    category.lower() == "download"
                    and len(Scoop_download) > 1
                    and Scoop_part_2
                ):
                    Scoop_download = " ".join(Scoop_download)
                    print(Scoop_download, sep="\n")
                    subprocess.call(Scoop_download, shell=True)
                    exit()
            elif isScoopinstalled.lower() == "n" or isScoopinstalled.lower() == "no":
                print("\n Installing Scoop (https://scoop.sh/) \n")
                subprocess.call(
                    "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser",
                    shell=True,
                )
                subprocess.call(
                    "Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression",
                    shell=True,
                )
                print("\x1B[2J")
                isScoopinstalled = "y"
                break
    elif source == "3" or source.capitalize() == os_list[2]:
        isWingetinstalled = input("Is Winget installed? Y/n...")
        while True:
            if (
                isWingetinstalled.lower() == "y"
                or isWingetinstalled.lower() == "yes"
                or isWingetinstalled == ""
            ):
                print("\x1B[2J")
                print("These are the options \n")
                for i in category_dic.items():
                    print(i, sep="\n")
                print("To start downloading procedure type download")
                category = input(
                    "Enter the corresponding number of the category you want to see..."
                )
                if category != "download" and int(category) in range(
                    1, len(category_dic)
                ):
                    search("windows", "winget", category)
                elif category.lower() == "download" and len(Winget_download) > 0:
                    Winget_download = "; ".join(Winget_download)
                    print(Winget_download, sep="\n")
                    subprocess.call(Winget_download, shell=True)
                    exit()
            elif isWingetinstalled.lower() == "n" or isWingetinstalled.lower() == "no":
                print(
                    "\n Installing Winget (https://learn.microsoft.com/en-us/windows/package-manager/winget/#install-winget) \n"
                )
                subprocess.call(
                    "Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe",
                    shell=True,
                )
                print("\x1B[2J")
                isWingetinstalled = "y"
                break
elif plat == "Linux":
    os_list = list(option[plat].keys())
    for i in range(len(os_list)):
        print(f"({i + 1}) {os_list[i]} \n")

    print("Please note that Apt is only supported for Debian based distros \n")
    print("Please note that Yay is only supported for Arch based distros \n")
    source = input("Please select your preferred Source...")
    if source == "1" or source.capitalize() == os_list[0]:
        while True:
            print("\x1B[2J")
            print("These are the options \n")
            for i in category_dic.items():
                print(i, sep="\n")
            print("To start downloading procedure type download")
            category = input(
                "Enter the corresponding number of the category you want to see..."
            )
            if category != "download" and int(category) in range(1, len(category_dic)):
                search("linux", "apt", category)
            elif (
                category.lower() == "download"
                and len(Apt_download) > 1
                and not Apt_part_2
            ):
                subprocess.call(Apt_part_1, shell=True)
                Apt_download = " ".join(Apt_download)
                print(Apt_download, sep="\n")
                subprocess.call(Apt_download, shell=True)
                exit()
            elif (
                category.lower() == "download" and len(Apt_download) > 1 and Apt_part_2
            ):
                Apt_download = " ".join(Apt_download)
                print(Apt_download, sep="\n")
                subprocess.call(Apt_download, shell=True)
                exit()
    elif source == "2" or source.capitalize() == os_list[1]:
        isFlatpakinstalled = input("Is Flatpak installed? Y/n... ")
        while True:
            if (
                isFlatpakinstalled.lower() == "y"
                or isFlatpakinstalled.lower() == "yes"
                or isFlatpakinstalled == ""
            ):
                print("\x1B[2J")
                print("These are the options \n")
                for i in category_dic.items():
                    print(i, sep="\n")
                print("To start downloading procedure type download")
                category = input(
                    "Enter the corresponding number of the category you want to see..."
                )
                if category != "download" and int(category) in range(
                    1, len(category_dic)
                ):
                    search("linux", "flatpak", category)
                elif category.lower() == "download" and len(Flatpak_download) > 1:
                    subprocess.call(Flatpak_part_1, shell=True)
                    Flatpak_download = " ".join(Flatpak_download)
                    print(Flatpak_download, sep="\n")
                    subprocess.call(Flatpak_download, shell=True)
                    break
            elif (
                isFlatpakinstalled.lower() == "n" or isFlatpakinstalled.lower() == "no"
            ):
                print(
                    "\n Please visit the url for setup instructions (https://flatpak.org/setup/) \n"
                )
                isFlatpakinstalled = input("Is Flatpak installed? Y/n... ")
                if (
                    isFlatpakinstalled.lower() == "y"
                    or isFlatpakinstalled.lower() == "yes"
                    or isFlatpakinstalled == ""
                ):
                    isFlatpakinstalled = "y"
                    print("\x1B[2J")
                    break
                else:
                    isFlatpakinstalled = "n"
                    break
    elif source == "3" or source.capitalize() == os_list[2]:
        isYayinstalled = input("Is Yay installed? Y/n...")
        while True:
            if (
                isYayinstalled.lower() == "y"
                or isYayinstalled.lower() == "yes"
                or isYayinstalled == ""
            ):
                print("\x1B[2J")
                print("These are the options \n")
                for i in category_dic.items():
                    print(i, sep="\n")
                print("To start downloading procedure type download")
                category = input(
                    "Enter the corresponding number of the category you want to see..."
                )
                if category != "download" and int(category) in range(
                    1, len(category_dic)
                ):
                    search("linux", "yay", category)
                elif category.lower() == "download" and len(Yay_download) > 1:
                    Yay_download = " ".join(Yay_download)
                    print(Yay_download, sep="\n")
                    subprocess.call(Yay_download, shell=True)
                    exit()
            elif isYayinstalled.lower() == "n" or isYayinstalled.lower() == "no":
                print(
                    "\n Installing Yay (https://github.com/Jguer/yay#installation) \n"
                )
                subprocess.call(
                    "sudo pacman -Syu --noconfirm git base-devel yay",
                    shell=True,
                )
                print("\x1B[2J")
                isYayinstalled = "y"
                break
elif plat == "Darwin":
    print(
        "\n Because your Operating System is MacOS, you will be using homebrew as the source \n"
    )

    ishomebrewinstalled = input("Is Homebrew installed? Y/n...")
    while True:
        if (
            ishomebrewinstalled.lower() == "y"
            or ishomebrewinstalled.lower() == "yes"
            or ishomebrewinstalled == ""
        ):
            print("\x1B[2J")
            print("These are the options \n")
            for i in category_dic.items():
                print(i, sep="\n")
            print("To start downloading procedure type download")
            category = input(
                "Enter the corresponding number of the category you want to see..."
            )
            if category != "download" and int(category) in range(1, len(category_dic)):
                search("MacOS", "homebrew", category)
            elif category.lower() == "download" and (
                len(selection_cask) > 1 or len(selection_formula) > 1
            ):
                if len(selection_cask) > 1:
                    selection_cask = " ".join(selection_cask)
                    if len(selection_formula) > 1:
                        selection_formula = " ".join(selection_formula)
                        selection = selection_cask + " ; " + selection_formula
                        print(selection, sep="\n")
                        subprocess.call(selection, shell=True)
                        exit()
                    else:
                        selection = selection_cask
                        print(selection, sep="\n")
                        subprocess.call(selection, shell=True)
                        exit()
                elif len(selection_cask) == 1 and len(selection_formula) > 1:
                    selection = " ".join(selection_formula)
                    print(selection, sep="\n")
                    subprocess.call(selection, shell=True)
                    exit()
        elif ishomebrewinstalled.lower() == "n" or ishomebrewinstalled.lower() == "no":
            print("\n Installing Homebrew (https://brew.sh) \n")
            subprocess.call(
                'sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                shell=True,
            )
            print("\x1B[2J")
            ishomebrewinstalled = "y"
            break
