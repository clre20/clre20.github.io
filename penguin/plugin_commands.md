# 伺服器插件指令與權限節點對照表

本文件提供本伺服器運行插件之指令、子命令、操作說明與權限節點對照，分類為玩家指令與管理員指令，供系統管理人員進行 LuckPerms 權限配置參考。

## 插件目錄索引

- [AdvancedSpyInventory](#advancedspyinventory)
- [AuraSkills](#auraskills)
- [AxAFKZone](#axafkzone)
- [BlockLocker](#blocklocker)
- [CMILib](#cmilib)
- [Cmail](#cmail)
- [CommandPanels](#commandpanels)
- [ConditionalEvents](#conditionalevents)
- [CoreProtect](#coreprotect)
- [DecentHolograms](#decentholograms)
- [DiscordLink](#discordlink)
- [DiscordSRV](#discordsrv)
- [DriveBackupV2](#drivebackupv2)
- [EggEmAll2](#eggemall2)
- [Elevator](#elevator)
- [Essentials](#essentials)
- [EssentialsWarpGUI](#essentialswarpgui)
- [EvenMoreFish](#evenmorefish)
- [ExcellentCrates](#excellentcrates)
- [ExecutableItems](#executableitems)
- [FeatherMorph](#feathermorph)
- [GSit](#gsit)
- [Geyser-Spigot](#geyser-spigot)
- [HeadDrop](#headdrop)
- [ImageFrame](#imageframe)
- [InsaneAnnouncer](#insaneannouncer)
- [InteractiveChat](#interactivechat)
- [InteractiveChatDiscordSrvAddon](#interactivechatdiscordsrvaddon)
- [LPC](#lpc)
- [LibsDisguises](#libsdisguises)
- [LiteSignIn](#litesignin)
- [LuckPerms](#luckperms)
- [MapLockPlus](#maplockplus)
- [MiniMOTD](#minimotd)
- [Multiverse-Core](#multiverse-core)
- [Multiverse-NetherPortals](#multiverse-netherportals)
- [MythicMobs](#mythicmobs)
- [PlaceholderAPI](#placeholderapi)
- [PlayerKits2](#playerkits2)
- [ProtocolLib](#protocollib)
- [QuickShop-Hikari](#quickshop-hikari)
- [Residence](#residence)
- [SCore](#score)
- [SetHome](#sethome)
- [Shopkeepers](#shopkeepers)
- [Simple_RTP](#simple_rtp)
- [SkBee](#skbee)
- [SkinsRestorer](#skinsrestorer)
- [Skript](#skript)
- [Slimefun](#slimefun)
- [SlimefunTranslation](#slimefuntranslation)
- [SphereLib](#spherelib)
- [SuperiorSkyblock2](#superiorskyblock2)
- [TAB](#tab)
- [TheosisEconomy](#theosiseconomy)
- [TownsAndNations](#townsandnations)
- [TpaGui](#tpagui)
- [Vault](#vault)
- [Veinminer](#veinminer)
- [ViaBackwards](#viabackwards)
- [ViaVersion](#viaversion)
- [VoidWorld](#voidworld)
- [WorldEdit](#worldedit)
- [WorldGuard](#worldguard)
- [ZNPCsPlus](#znpcsplus)
- [eShulkerBox](#eshulkerbox)
- [floodgate](#floodgate)
- [nightcore](#nightcore)
- [packetevents](#packetevents)
- [playerHead](#playerhead)
- [qsaddon-discordsrv](#qsaddon-discordsrv)

---

## <a id="advancedspyinventory"></a>AdvancedSpyInventory
* 檔案路徑: [`plugins/AdvancedSpyInventory-2.4.13.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/AdvancedSpyInventory-2.4.13.jar)
* 功能概述: Open and modify the 背包 of entities and 玩家, and the 末影箱 of the 玩家, online or not!

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> [Player]` | ec | Open 末影箱 of 玩家 | `advancedspyinventory.enderchest` |
| `/<command> <Player|Entity>` | - | Open 背包 of 玩家 and entities | `advancedspyinventory.inventory` |


---

## <a id="auraskills"></a>AuraSkills
* 檔案路徑: [`plugins/AuraSkills-2.3.12.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/AuraSkills-2.3.12.jar)
* 功能概述: RPG技能與被動屬性加成系統。提供採礦、挖掘、戰鬥等技能升級，藉此獲得生命值、力量等屬性加成與主被動技能。

#### 查詢說明：
1. **查詢技能進度**：輸入 `/skills` 開啟主選單 GUI，查看各項技能等級與經驗。
2. **查詢屬性加成**：輸入 `/stats` 查看因技能升級所帶來的生命上限、暴擊率等被動屬性增益。
3. **經驗獲取**：於伺服器中進行挖掘、砍樹、挖礦或擊殺怪物等常規操作，即可自動累加對應技能經驗。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/skills` | /stats | 開啟技能與屬性的核心 GUI 選單面板。 | `auraskills.command.skills` |
| `/skills top [技能名稱]` | - | 查看伺服器中特定技能或總等級最高的玩家排行榜。 | `auraskills.command.top` |
| `/skillsstats` | /stats | 直接查看自身的基礎屬性被動增益面板。 | `auraskills.command.stats` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/auraskills reload` | - | 重新載入 AuraSkills 技能插件的所有 YAML 設定檔。 | `auraskills.command.admin` |
| `/auraskills xp add <玩家> <技能> <數值>` | - | 管理員指令：為玩家直接增加特定技能的經驗值。 | `auraskills.command.admin` |
| `/auraskills xp set <玩家> <技能> <數值>` | - | 管理員指令：將玩家的特定技能等級/經驗直接修改為指定數值。 | `auraskills.command.admin` |


---

## <a id="axafkzone"></a>AxAFKZone
* 檔案路徑: [`plugins/AxAFKZone-1.12.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/AxAFKZone-1.12.0.jar)

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `axafkzone.bypass.iplimit` | - | `False` |
| `axafkzone.create` | - | `op` |
| `axafkzone.delete` | - | `op` |
| `axafkzone.help` | - | `op` |
| `axafkzone.redefine` | - | `op` |
| `axafkzone.reload` | - | `op` |
| `axafkzone.tp` | - | `op` |
| `axafkzone.wand` | - | `op` |


---

## <a id="blocklocker"></a>BlockLocker
* 檔案路徑: [`plugins/blocklocker-1.14.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/blocklocker-1.14.1.jar)

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> reload` | bl | Administration 指令 for BlockLocker. | `blocklocker.reload` |


---

## <a id="cmilib"></a>CMILib
* 檔案路徑: [`plugins/CMILib1.5.9.9.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/CMILib1.5.9.9.jar)
* 功能概述: CMI library

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/cmil` | - | basic 指令 | `無` |


---

## <a id="cmail"></a>Cmail
* 檔案路徑: [`plugins/cmail-6.2.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/cmail-6.2.3.jar)
* 功能概述: A Minecraft Mail plugin

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/cmail [mail|send]` | [mail] | 郵件主命令 | `cmail.use` |


---

## <a id="commandpanels"></a>CommandPanels
* 檔案路徑: [`plugins/CommandPanels.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/CommandPanels.jar)
* 功能概述: Fully Custom Interactive GUIs with Animations and Logic.

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="conditionalevents"></a>ConditionalEvents
* 檔案路徑: [`plugins/ConditionalEvents-4.79.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ConditionalEvents-4.79.1.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/conditionalevents` | ce | Main 指令 of ConditionalEvents | `無` |


---

## <a id="coreprotect"></a>CoreProtect
* 檔案路徑: [`plugins/CoreProtect-CE-24.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/CoreProtect-CE-24.0.jar)
* 功能概述: 方塊變更記錄與回滾工具。可記錄方塊破壞/放置、容器存取、熔爐、點火與門的開關歷史。

#### 系統操作說明：
1. **啟用查詢模式**：輸入 `/co inspect` 或 `/co i`。系統提示啟用後，進行以下操作：
   * **滑鼠左鍵** 點擊任何方塊，可查詢該位置方塊的歷史破壞記錄。
   * **滑鼠右鍵** 點擊任何方塊表面，可查詢該方塊的放置者與時間。
   * **滑鼠右鍵** 點擊容器（箱子、熔爐、漏斗等），可查詢容器內物品的存取歷史記錄。
2. **停用查詢模式**：再次輸入 `/co i`。
3. **執行操作回滾 (Rollback)**：當區域遭受破壞，可使用回滾命令復原。
   * 格式範例：`/co rollback u:steve t:2h r:20` (將玩家 `steve` 於半徑 `20` 格內、`2` 小時內的所有操作進行回滾)。

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/co inspect (或 /co i)` | /co i | 啟用/停用查詢模式。啟用後點擊方塊或容器可查詢歷史操作記錄。 | `coreprotect.inspect` |
| `/co lookup <參數> (或 /co l ...)` | /co l | 查詢數據庫記錄並以列表輸出詳細歷史資訊。 | `coreprotect.lookup` |
| `/co purge t:<時間>` | - | 清理指定時間之前的歷史記錄以釋放硬碟空間。範例：`/co purge t:30d` (刪除 30 天前的記錄)。 | `coreprotect.purge` |
| `/co reload` | - | 重新載入 CoreProtect 配置文件。 | `coreprotect.reload` |
| `/co restore <參數>` | - | 還原回滾操作（復原非預期的回滾動作）。 | `coreprotect.restore` |
| `/co rollback <參數> (或 /co rb ...)` | /co rb | 執行回滾操作。支援參數：`u:<玩家>`、`t:<時間(如 1h, 2d)>`、`r:<半徑(如 10 或 global)>`、`a:<動作(如 +block)>`。 | `coreprotect.rollback` |


---

## <a id="decentholograms"></a>DecentHolograms
* 檔案路徑: [`plugins/DecentHolograms-2.10.1-MODIFIED.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/DecentHolograms-2.10.1-MODIFIED.jar)
* 功能概述: A lightweight yet very powerful 全息浮空字 plugin with many features and 設定檔 options.

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `dh.admin` | Allows 玩家 to use DecentHolograms. | `op` |
| `dh.command` | Allows 玩家 to use all 指令 of DecentHolograms | `op` |
| `dh.command.convert` | Allows 玩家 to use the 指令 '/dh convert <plugin> | `op` |
| `dh.command.decentholograms` | Allows 玩家 to use the 指令 '/decentholograms | `op` |
| `dh.command.displays` | Allows 玩家 to use the 指令 '/dh 顯示' and all its sub-指令 | `op` |
| `dh.command.displays.attribute` | Allows 玩家 to use the 指令 '/dh 顯示 attribute <顯示> <attribute> [value] | `op` |
| `dh.command.displays.center` | Allows 玩家 to use the 指令 '/dh 顯示 center <顯示> | `op` |
| `dh.command.displays.clone` | Allows 玩家 to use the 指令 '/dh 顯示 clone <顯示> <new_name> | `op` |
| `dh.command.displays.create` | Allows 玩家 to use the 指令 '/dh 顯示 創建 <type> <name> [content] | `op` |
| `dh.command.displays.delete` | Allows 玩家 to use the 指令 '/dh 顯示 刪除 <顯示> | `op` |
| `dh.command.displays.disable` | Allows 玩家 to use the 指令 '/dh 顯示 disable <顯示> | `op` |
| `dh.command.displays.displayrange` | Allows 玩家 to use the 指令 '/dh 顯示 顯示-range <顯示> <range> | `op` |
| `dh.command.displays.enable` | Allows 玩家 to use the 指令 '/dh 顯示 enable <顯示> | `op` |
| `dh.command.displays.facing` | Allows 玩家 to use the 指令 '/dh 顯示 set-facing <顯示> <yaw> [pitch] | `op` |
| `dh.command.displays.help` | Allows 玩家 to use the 指令 '/dh 顯示 help | `op` |
| `dh.command.displays.list` | Allows 玩家 to use the 指令 '/dh 顯示 list [page] | `op` |
| `dh.command.displays.listattributes` | Allows 玩家 to use the 指令 '/dh 顯示 list-attributes <顯示> | `op` |
| `dh.command.displays.move` | Allows 玩家 to use the 指令 '/dh 顯示 move <顯示> <x> <y> <z> | `op` |
| `dh.command.displays.movehere` | Allows 玩家 to use the 指令 '/dh 顯示 movehere <顯示> | `op` |
| `dh.command.displays.nearby` | Allows 玩家 to use the 指令 '/dh 顯示 nearby <range> [page] | `op` |
| `dh.command.displays.rename` | Allows 玩家 to use the 指令 '/dh 顯示 rename <顯示> <new_name> | `op` |
| `dh.command.displays.resetattribute` | Allows 玩家 to use the 指令 '/dh 顯示 reset-attribute <顯示> <attribute> | `op` |
| `dh.command.displays.setblock` | Allows 玩家 to use the 指令 '/dh 顯示 set-block <顯示> <block_type> | `op` |
| `dh.command.displays.setitem` | Allows 玩家 to use the 指令 '/dh 顯示 set-item <顯示> <item> | `op` |
| `dh.command.displays.teleport` | Allows 玩家 to use the 指令 '/dh 顯示 傳送 <顯示> | `op` |
| `dh.command.displays.text.addline` | Allows 玩家 to use the 指令 '/dh 顯示 add-line <顯示> <text> | `op` |
| `dh.command.displays.text.insertline` | Allows 玩家 to use the 指令 '/dh 顯示 insert-line <顯示> <index> <text> | `op` |
| `dh.command.displays.text.removeline` | Allows 玩家 to use the 指令 '/dh 顯示 remove-line <顯示> <index> | `op` |
| `dh.command.displays.text.setline` | Allows 玩家 to use the 指令 '/dh 顯示 set-line <顯示> <index> <text> | `op` |
| `dh.command.displays.text.swaplines` | Allows 玩家 to use the 指令 '/dh 顯示 swap-lines <顯示> <index1> <index2> | `op` |
| `dh.command.displays.updateinterval` | Allows 玩家 to use the 指令 '/dh 顯示 update-interval <顯示> <interval> | `op` |
| `dh.command.features` | Allows 玩家 to use the 指令 '/dh features' and all its sub-指令 | `op` |
| `dh.command.features.disable` | Allows 玩家 to use the 指令 '/dh features disable <feature> | `op` |
| `dh.command.features.enable` | Allows 玩家 to use the 指令 '/dh features enable <feature> | `op` |
| `dh.command.features.help` | Allows 玩家 to use the 指令 '/dh features help | `op` |
| `dh.command.features.info` | Allows 玩家 to use the 指令 '/dh features info <feature> | `op` |
| `dh.command.features.list` | Allows 玩家 to use the 指令 '/dh features list | `op` |
| `dh.command.features.reload` | Allows 玩家 to use the 指令 '/dh features 重新載入 | `op` |
| `dh.command.help` | Allows 玩家 to use the 指令 '/dh help | `op` |
| `dh.command.holograms` | Allows 玩家 to use the 指令 '/dh 全息浮空字' and all its sub-指令 | `op` |
| `dh.command.holograms.addflag` | Allows 玩家 to use the 指令 '/dh 全息浮空字 addflag <全息浮空字> <flag> | `op` |
| `dh.command.holograms.align` | Allows 玩家 to use the 指令 '/dh 全息浮空字 align <全息浮空字> <X|Y|Z|XZ|FACE> <otherHologram> | `op` |
| `dh.command.holograms.center` | Allows 玩家 to use the 指令 '/dh 全息浮空字 center <全息浮空字> | `op` |
| `dh.command.holograms.clone` | Allows 玩家 to use the 指令 '/dh 全息浮空字 clone <全息浮空字> <name> [temp] [-l:<世界>:<x>:<y>:<z>] | `op` |
| `dh.command.holograms.create` | Allows 玩家 to use the 指令 '/dh 全息浮空字 創建 <name> [-l:<世界>:<x>:<y>:<z>] [content] | `op` |
| `dh.command.holograms.delete` | Allows 玩家 to use the 指令 '/dh 全息浮空字 刪除 <全息浮空字> | `op` |
| `dh.command.holograms.disable` | Allows 玩家 to use the 指令 '/dh 全息浮空字 disable <全息浮空字> | `op` |
| `dh.command.holograms.downorigin` | Allows 玩家 to use the 指令 '/dh 全息浮空字 downorigin <全息浮空字> <true|false> | `op` |
| `dh.command.holograms.enable` | Allows 玩家 to use the 指令 '/dh 全息浮空字 enable <全息浮空字> | `op` |
| `dh.command.holograms.help` | Allows 玩家 to use the 指令 '/dh 全息浮空字 help | `op` |
| `dh.command.holograms.info` | Allows 玩家 to use the 指令 '/dh 全息浮空字 info <全息浮空字> | `op` |
| `dh.command.holograms.lines` | Allows 玩家 to use the 指令 '/dh 全息浮空字 lines <全息浮空字> <page> [listPage] | `op` |
| `dh.command.holograms.move` | Allows 玩家 to use the 指令 '/dh 全息浮空字 move <全息浮空字> <x> <y> <z> | `op` |
| `dh.command.holograms.movehere` | Allows 玩家 to use the 指令 '/dh 全息浮空字 movehere <全息浮空字> | `op` |
| `dh.command.holograms.near` | Allows 玩家 to use the 指令 '/dh 全息浮空字 near <range> | `op` |
| `dh.command.holograms.removeflag` | Allows 玩家 to use the 指令 '/dh 全息浮空字 removeflag <全息浮空字> <flag> | `op` |
| `dh.command.holograms.rename` | Allows 玩家 to use the 指令 '/dh 全息浮空字 rename <全息浮空字> <new_name> | `op` |
| `dh.command.holograms.setdisplayrange` | Allows 玩家 to use the 指令 '/dh 全息浮空字 setdisplayrange <全息浮空字> <range> | `op` |
| `dh.command.holograms.setfacing` | Allows 玩家 to use the 指令 '/dh 全息浮空字 setfacing <全息浮空字> <facing> | `op` |
| `dh.command.holograms.setpermission` | Allows 玩家 to use the 指令 '/dh 全息浮空字 setpermission <全息浮空字> [權限] | `op` |
| `dh.command.holograms.setupdateinterval` | Allows 玩家 to use the 指令 '/dh 全息浮空字 setupdateinterval <全息浮空字> <interval> | `op` |
| `dh.command.holograms.setupdaterange` | Allows 玩家 to use the 指令 '/dh 全息浮空字 setupdaterange <全息浮空字> <range> | `op` |
| `dh.command.holograms.teleport` | Allows 玩家 to use the 指令 '/dh 全息浮空字 傳送 <全息浮空字> | `op` |
| `dh.command.holograms.update` | Allows 玩家 to use the 指令 '/dh 全息浮空字 update <全息浮空字> | `op` |
| `dh.command.lines` | Allows 玩家 to use the 指令 '/dh lines' and all its sub-指令 | `op` |
| `dh.command.lines.add` | Allows 玩家 to use the 指令 '/dh lines add <全息浮空字> <page> [content] | `op` |
| `dh.command.lines.addflag` | Allows 玩家 to use the 指令 '/dh lines addflag <全息浮空字> <page> <line> <flag> | `op` |
| `dh.command.lines.align` | Allows 玩家 to use the 指令 '/dh lines align <全息浮空字> <page> <line1> <line2> <X|Z|XZ|FACE> | `op` |
| `dh.command.lines.edit` | Allows 玩家 to use the 指令 '/dh lines 編輯 <全息浮空字> <page> <line> | `op` |
| `dh.command.lines.height` | Allows 玩家 to use the 指令 '/dh lines height <全息浮空字> <page> <line> <height> | `op` |
| `dh.command.lines.help` | Allows 玩家 to use the 指令 '/dh lines help | `op` |
| `dh.command.lines.info` | Allows 玩家 to use the 指令 '/dh lines info <全息浮空字> <page> <line> | `op` |
| `dh.command.lines.insert` | Allows 玩家 to use the 指令 '/dh lines insert <全息浮空字> <page> <line> [content] | `op` |
| `dh.command.lines.offsetx` | Allows 玩家 to use the 指令 '/dh lines offsetx <全息浮空字> <page> <line> <offset> | `op` |
| `dh.command.lines.offsetz` | Allows 玩家 to use the 指令 '/dh lines offsetz <全息浮空字> <page> <line> <offset> | `op` |
| `dh.command.lines.remove` | Allows 玩家 to use the 指令 '/dh lines remove <全息浮空字> <page> <line> | `op` |
| `dh.command.lines.removeflag` | Allows 玩家 to use the 指令 '/dh lines removeflag <全息浮空字> <page> <line> <flag> | `op` |
| `dh.command.lines.set` | Allows 玩家 to use the 指令 '/dh lines set <全息浮空字> <page> <line> <content> | `op` |
| `dh.command.lines.setfacing` | Allows 玩家 to use the 指令 '/dh lines setfacing <全息浮空字> <page> <line> <facing> | `op` |
| `dh.command.lines.setpermission` | Allows 玩家 to use the 指令 '/dh lines setpermission <全息浮空字> <page> <line> [權限] | `op` |
| `dh.command.lines.swap` | Allows 玩家 to use the 指令 '/dh lines swap <全息浮空字> <page> <line1> <line2> | `op` |
| `dh.command.list` | Allows 玩家 to use the 指令 '/dh list [page] | `op` |
| `dh.command.pages` | Allows 玩家 to use the 指令 '/dh pages' and all its sub-指令 | `op` |
| `dh.command.pages.actions` | Allows 玩家 to use the 指令 '/dh pages actions <全息浮空字> <page> <clickType> [listPage] | `op` |
| `dh.command.pages.add` | Allows 玩家 to use the 指令 '/dh pages add <全息浮空字> [content] | `op` |
| `dh.command.pages.addaction` | Allows 玩家 to use the 指令 '/dh pages addaction <全息浮空字> <page> <clickType> <action> | `op` |
| `dh.command.pages.clearactions` | Allows 玩家 to use the 指令 '/dh pages clearactions <全息浮空字> <page> <clickType> | `op` |
| `dh.command.pages.help` | Allows 玩家 to use the 指令 '/dh pages help | `op` |
| `dh.command.pages.insert` | Allows 玩家 to use the 指令 '/dh pages insert <全息浮空字> <page> [content] | `op` |
| `dh.command.pages.remove` | Allows 玩家 to use the 指令 '/dh pages remove <全息浮空字> <page> | `op` |
| `dh.command.pages.removeaction` | Allows 玩家 to use the 指令 '/dh pages removeaction <全息浮空字> <page> <clickType> <index> | `op` |
| `dh.command.pages.swap` | Allows 玩家 to use the 指令 '/dh pages swap <全息浮空字> <page1> <page2> | `op` |
| `dh.command.pages.switch` | Allows 玩家 to use the 指令 '/dh pages switch <全息浮空字> <page> [玩家] | `op` |
| `dh.command.profiler` | Allows 玩家 to use the 指令 '/dh profiler' and all its sub-指令 | `op` |
| `dh.command.profiler.help` | Allows 玩家 to use the 指令 '/dh profiler help | `op` |
| `dh.command.profiler.reset` | Allows 玩家 to use the 指令 '/dh profiler reset [timer] | `op` |
| `dh.command.profiler.start` | Allows 玩家 to use the 指令 '/dh profiler start | `op` |
| `dh.command.profiler.stats` | Allows 玩家 to use the 指令 '/dh profiler stats [timer] | `op` |
| `dh.command.profiler.stop` | Allows 玩家 to use the 指令 '/dh profiler stop | `op` |
| `dh.command.reload` | Allows 玩家 to use the 指令 '/dh 重新載入 | `op` |
| `dh.command.version` | Allows 玩家 to use the 指令 '/dh version | `op` |
| `dh.default` | Allows 玩家 to see the version after using '/decentholograms'. | `True` |


---

## <a id="discordlink"></a>DiscordLink
* 檔案路徑: [`plugins/DiscordLink-1.6.7.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/DiscordLink-1.6.7.jar)
* 功能概述: A Discord Link plugin

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/discordlink` | [dclink] | DiscordLink 系統指令 | `discordlink.admin` |


---

## <a id="discordsrv"></a>DiscordSRV
* 檔案路徑: [`plugins/DiscordSRV-Build-1.30.5.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/DiscordSRV-Build-1.30.5.jar)
* 功能概述: The most powerful, configurable, open-source Discord bridge plugin out there.

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `|` | [discordsrv] | DiscordSRV 指令 | `discordsrv.discord` |


---

## <a id="drivebackupv2"></a>DriveBackupV2
* 檔案路徑: [`plugins/DriveBackupV2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/DriveBackupV2.jar)
* 功能概述: Uploads backups to Google Drive/OneDrive or by (S)FTP

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/drivebackup` | - | 查看 all DriveBackupV2 指令 | `無` |


---

## <a id="eggemall2"></a>EggEmAll2
* 檔案路徑: [`plugins/EggEmAll2-2.1.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/EggEmAll2-2.1.1.jar)

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `eggemall.all` | Gives access to catch all types of mobs. | `op` |


---

## <a id="elevator"></a>Elevator
* 檔案路徑: [`plugins/Elevator.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Elevator.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="essentials"></a>Essentials
* 檔案路徑: [`plugins/EssentialsX-2.22.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/EssentialsX-2.22.0.jar)
* 功能概述: 基礎命令與行政工具包。提供基礎傳送、家門地標設定、轉帳交易、狀態控制及後台管理。

#### 常用功能說明：
1. **設置家與傳送**：
   * 於指定位置輸入 `/sethome [家名稱]` (預設為 `home`) 即可儲存傳送點。
   * 輸入 `/home [家名稱]` 可瞬間返回該存檔位置。
2. **玩家互傳 (TPA)**：
   * 輸入 `/tpa <目標玩家>` 發送傳送請求。
   * 接收者可輸入 `/tpaccept` 接受或 `/tpdeny` 拒絕該請求。
3. **返還前一位置**：
   * 傳送後或死亡後，可輸入 `/back` 返回前一站立點或最近的死亡坐標。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/afk` | - | 將自身的狀態切換為「掛機中」，再次輸入即可關閉。 | `essentials.afk` |
| `/back` | - | 傳送回上一次的所在地點或最近一次的死亡地點。 | `essentials.back` |
| `/bal (或 /balance)` | /bal | 查詢自身錢包目前的餘額。 | `essentials.balance` |
| `/delhome [名稱]` | - | 刪除指定的家。 | `essentials.delhome` |
| `/home [名稱]` | - | 傳送到您設置的家。 | `essentials.home` |
| `/pay <玩家> <金額>` | - | 從個人錢包內轉帳指定的金幣給其他玩家。 | `essentials.pay` |
| `/sethome [名稱]` | - | 將目前的站立點設置為一個家。 | `essentials.sethome` |
| `/spawn` | - | 傳送回伺服器的主出生點/生成點。 | `essentials.spawn` |
| `/tpa <玩家>` | - | 向目標玩家發送傳送請求（請求傳送到他身邊）。 | `essentials.tpa` |
| `/tpaccept` | - | 接受其他玩家發送給您的傳送邀請。 | `essentials.tpaccept` |
| `/tpdeny` | - | 拒絕其他玩家發送給您的傳送邀請。 | `essentials.tpdeny` |
| `/warp [地標名稱]` | - | 傳送到管理員設置的公共傳送點。 | `essentials.warp` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/ban <玩家> [原因]` | - | 管理員指令：永久封禁指定玩家使其無法加入伺服器。 | `essentials.ban` |
| `/essentials reload` | - | 管理員指令：重新載入 Essentials 插件的所有配置。 | `essentials.reload` |
| `/feed [玩家]` | - | 管理員指令：將指定玩家的飢餓度補滿。 | `essentials.feed` |
| `/fly [玩家]` | - | 管理員指令：開啟或關閉飛行狀態。 | `essentials.fly` |
| `/gamemode <模式> [玩家]` | /gmc, /gms, /gma, /gmsp | 管理員指令：切換自己或指定玩家的遊戲模式（創造/生存/冒險/旁觀）。 | `essentials.gamemode` |
| `/heal [玩家]` | - | 管理員指令：將指定玩家的生命值與飢餓度補滿，並解除負面效果。 | `essentials.heal` |
| `/kick <玩家> [原因]` | - | 管理員指令：強制踢出指定玩家。 | `essentials.kick` |
| `/mute <玩家> [時間]` | - | 管理員指令：禁止指定玩家在聊天室發送訊息。 | `essentials.mute` |
| `/tp <玩家1> [玩家2]` | - | 管理員指令：強制將自己傳送到某玩家，或將玩家1傳送給玩家2。 | `essentials.tp` |
| `/tphere <玩家>` | - | 管理員指令：強制將指定玩家傳送到自己當前位置。 | `essentials.tphere` |
| `/vanish (或 /v)` | /v | 管理員指令：隱身，使一般玩家無法在伺服器中看見您，也不會在 Tab 顯示。 | `essentials.vanish` |


---

## <a id="essentialswarpgui"></a>EssentialsWarpGUI
* 檔案路徑: [`plugins/WarpGUI.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/WarpGUI.jar)
* 功能概述: Opens a gorgeous GUI for 地標傳送點 selection

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/warpcfg [args...]` | [ warpconfig, warpscfg, warpsconfig ] | Modify the look-and-feel of the warps | `warpcfg.cfg` |


---

## <a id="evenmorefish"></a>EvenMoreFish
* 檔案路徑: [`plugins/even-more-fish-2.1.14-1.21.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/even-more-fish-2.1.14-1.21.jar)
* 功能概述: A fishing extension bringing an exciting new experience to fishing.

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `emf.*` | - | `op` |
| `emf.admin` | - | `op` |
| `emf.admin.migrate` | Allows users to use the migrate 指令. | `op` |
| `emf.admin.update.notify` | Allows users to be notified about updates. | `op` |
| `emf.applybaits` | Allows users to apply baits to rods. | `op` |
| `emf.help` | Allows users to see the help messages. | `True` |
| `emf.journal` | Allows access to the fish journal. | `op` |
| `emf.next` | Allows users to see when the next competition will be. | `op` |
| `emf.sellall` | Allows users to use sellall. | `op` |
| `emf.shop` | Allows users to use /emf 商店. | `op` |
| `emf.toggle` | Allows users to 切換 emf. | `op` |
| `emf.top` | Allows users to use /emf top. | `op` |
| `emf.use_rod` | Allows users to use emf rods. | `op` |
| `emf.user` | - | `op` |


---

## <a id="excellentcrates"></a>ExcellentCrates
* 檔案路徑: [`plugins/ExcellentCrates-6.6.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ExcellentCrates-6.6.1.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="executableitems"></a>ExecutableItems
* 檔案路徑: [`plugins/ExecutableItems-7.26.7.5.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ExecutableItems-7.26.7.5.jar)
* 功能概述: Custom Items, run 指令 with item, send message, 創建 boost item with delay, set cooldown !!

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> [ reload | give | giveusage | givealluage | giveslot | giveall | show | editor | edit | actionbar | refresh | create | take | drop | clear | delete ]` | - | ei 指令 | `ei.*` |


---

## <a id="feathermorph"></a>FeatherMorph
* 檔案路徑: [`plugins/feathermorph-2.8.1-1.21.11-final.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/feathermorph-2.8.1-1.21.11-final.jar)
* 功能概述: Yet another disguise plugin, that introduces the morph feature to the\

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `feathermorph.ability` | - | `True` |
| `feathermorph.acquire_morph` | - | `True` |
| `feathermorph.admin` | - | `op` |
| `feathermorph.can_fly` | - | `True` |
| `feathermorph.can_fly.always` | - | `False` |
| `feathermorph.chatoverride` | - | `True` |
| `feathermorph.custom_skin` | - | `op` |
| `feathermorph.custom_text` | - | `True` |
| `feathermorph.disguise_properties.custom_skin_on_items` | - | `op` |
| `feathermorph.disguise_properties.use` | - | `True` |
| `feathermorph.disguise_revealing` | - | `op` |
| `feathermorph.disguise_use_real_uuid` | - | `False` |
| `feathermorph.headmorph` | - | `True` |
| `feathermorph.lookup` | - | `op` |
| `feathermorph.magic_bottle.exclude` | - | `False` |
| `feathermorph.magic_bottle.use` | - | `True` |
| `feathermorph.make_disguise_tool` | - | `op` |
| `feathermorph.manage` | - | `op` |
| `feathermorph.manage.grant` | - | `op` |
| `feathermorph.manage.morph` | - | `op` |
| `feathermorph.manage.revoke` | - | `op` |
| `feathermorph.manage.unmorph` | - | `op` |
| `feathermorph.mirror` | - | `True` |
| `feathermorph.mirror.immune` | - | `op` |
| `feathermorph.mirror.mannequin` | - | `False` |
| `feathermorph.morph` | - | `True` |
| `feathermorph.query` | - | `op` |
| `feathermorph.queryall` | - | `op` |
| `feathermorph.reload` | - | `op` |
| `feathermorph.request` | - | `True` |
| `feathermorph.request.accept` | - | `True` |
| `feathermorph.request.deny` | - | `True` |
| `feathermorph.request.send` | - | `True` |
| `feathermorph.skill` | - | `True` |
| `feathermorph.skin_cache` | - | `op` |
| `feathermorph.stat` | - | `op` |
| `feathermorph.switch_backend` | - | `op` |
| `feathermorph.toggle` | - | `op` |
| `feathermorph.toggle_town_fly` | - | `True` |
| `feathermorph.unmorph` | - | `True` |


---

## <a id="gsit"></a>GSit
* 檔案路徑: [`plugins/GSit-3.5.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/GSit-3.5.1.jar)
* 功能概述: Relax with other 玩家 on nice seats!

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> [toggle]` | [crawl] | Crawl 指令 | `無` |
| `/<command>` | [lay] | Lay 指令 | `GSit.Lay` |
| `/<command>` | [layback] | Lay back 指令 | `GSit.LayBack` |
| `/<command> [toggle|playertoggle]` | [sit] | Sit 指令 | `GSit.*` |
| `/<command>` | [spin] | Spin 指令 | `GSit.Spin` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command>` | [bellyflop] | Bellyflop 指令 | `GSit.Bellyflop` |
| `/<command>` | [gsitrl] | Plugin 重新載入 指令 | `GSit.Reload` |


---

## <a id="geyser-spigot"></a>Geyser-Spigot
* 檔案路徑: [`plugins/Geyser-Spigot.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Geyser-Spigot.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="headdrop"></a>HeadDrop
* 檔案路徑: [`plugins/HeadDrop-Free.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/HeadDrop-Free.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/head <playername>` | - | Get 玩家 head | `headdrop.head` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/headdrop` | - | Main 指令 of HeadDrop plugin | `headdrop.reload` |


---

## <a id="imageframe"></a>ImageFrame
* 檔案路徑: [`plugins/ImageFrame-1.9.0.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ImageFrame-1.9.0.0.jar)
* 功能概述: Put images on maps and walls!

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/imageframe` | [iframe, if, frame] | Plugin main 指令 | `imageframe.create` |


---

## <a id="insaneannouncer"></a>InsaneAnnouncer
* 檔案路徑: [`plugins/InsaneAnnouncer-1.4.9.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/InsaneAnnouncer-1.4.9.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="interactivechat"></a>InteractiveChat
* 檔案路徑: [`plugins/InteractiveChat-4.3.5.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/InteractiveChat-4.3.5.0.jar)
* 功能概述: Make the chat interactive

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command>` | [ic] | Plugin main 指令 | `interactivechat.reload` |


---

## <a id="interactivechatdiscordsrvaddon"></a>InteractiveChatDiscordSrvAddon
* 檔案路徑: [`plugins/InteractiveChatDiscordSrvAddon-4.3.5.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/InteractiveChatDiscordSrvAddon-4.3.5.0.jar)
* 功能概述: DiscordSRV addon to InteractiveChat

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command>` | [icd] | Plugin main 指令 | `interactivechatdiscordsrv.reloadconfig` |


---

## <a id="lpc"></a>LPC
* 檔案路徑: [`plugins/LPC-3.7.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/LPC-3.7.1.jar)
* 功能概述: A chat formatting plugin for LuckPerms.

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `Usage: /lpc <reload|clear|debug>` | - | LPC 指令. | `lpc.reload` |


---

## <a id="libsdisguises"></a>LibsDisguises
* 檔案路徑: [`plugins/LibsDisguises-11.0.18-Free.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/LibsDisguises-11.0.18-Free.jar)
* 功能概述: A disguise plugin with various disguises.

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/disguise` | [ d, dis, disg ] | Disguise yourself as an entity. | `libsdisguises.seecmd.disguise` |
| `/disguiseanimation` | - | Play a supported animation on your own disguise | `libsdisguises.disguiseanimation` |
| `/disguiseentity` | [ dentity, disentity, disgentity ] | Disguise an entity as another entity. | `libsdisguises.seecmd.disguiseentity` |
| `/disguiseentityanimation` | - | Play a supported animation on a right clicked entity's disguise | `libsdisguises.disguiseentityanimation` |
| `/disguisehelp` | [ dhelp, dishelp, disghelp ] | Help 指令 for LibsDisguises. | `libsdisguises.seecmd.disguisehelp` |
| `/disguiseplayer` | [ dplayer, displayer, disgplayer, disguiseuuid, disguuid, duuid ] | Disguise another 玩家 as an entity. | `libsdisguises.seecmd.disguiseplayer` |
| `/disguiseplayeranimation` | [ disguiseuuidanimation ] | Play a supported animation on a 玩家/uuid's disguise | `libsdisguises.disguiseplayeranimation` |
| `/disguiseradius` | [ disradius, dradius, disgradius ] | Disguise all entities within a radius as an entity. | `libsdisguises.seecmd.disguiseradius` |
| `/disguiseradiusanimation` | - | Play a supported animation on all supported disguises in a radius | `libsdisguises.disguiseradiusanimation` |
| `/disguiseselector` | [ dselector, disselector, disgselector ] | Disguise entities via entity selector. | `libsdisguises.seecmd.disguiseselector` |
| `/disguiseselectoranimation` | - | Play a supported animation on all supported disguises via entity selector. | `libsdisguises.disguiseselectoranimation` |
| `/disguiseviewbar` | [ dviewbar, dvb, disguisevb, disvb, viewdisguisebar, viewbardisguise, bardisguise, bardisg, bard, | 切換 seeing your own disguise on or off. | `libsdisguises.seecmd.disguiseviewbar` |
| `/disguiseviewself` | [ dviewself, dvs, disguisevs, disvs, vsd, viewselfdisguise, viewselfd, selfdisguise, selfdisg, selfd, toggleselfdisguise, seeselfdisguise ] | 切換 seeing your own disguise on or off. | `libsdisguises.seecmd.disguiseviewself` |
| `/grabhead` | [ grabskull, playerhead, savehead, gethead ] | Grab the head item of a 皮膚, url or 玩家 | `libsdisguises.seecmd.grabhead` |
| `/grabskin` | [ uploadskin, skin, saveskin, cacheskin, downloadskin, skincache ] | Grab a 皮膚 from file, url or 玩家 name/uuid | `libsdisguises.seecmd.grabskin` |
| `/libsdisguises` | [ libsdisg, ld ] | Main 指令 for libsdisguises. | `libsdisguises.reload` |
| `/undisguise` | [ und, undis, undisg ] | Undisguise yourself. | `libsdisguises.seecmd.undisguise` |
| `/undisguiseentity` | [ undisentity, undentity, undisgentity ] | Undisguise an entity. | `libsdisguises.seecmd.undisguiseentity` |
| `/undisguiseplayer` | [ undisplayer, undplayer, undisgplayer, undisguiseuuid, unduuid, undisguuid ] | Undisguise a 玩家. | `libsdisguises.seecmd.undisguiseplayer` |
| `/undisguiseradius` | [ undisradius, undradius, undisgradius ] | Undisguise all entities within a radius. | `libsdisguises.seecmd.undisguiseradius` |
| `/undisguiseselector` | [ undisselector, undselector, undisgselector ] | Undisguise all entities in an entity selector. | `libsdisguises.seecmd.undisguiseselector` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/copydisguise` | [ disguisecopy, disgcopy, dcopy, copydisg, copyd, parsedisguise, disguiseparse ] | Output a disguise to a usable string | `libsdisguises.seecmd.copydisguise` |
| `/disguiseclone` | [ disguisec, disc, disclone, dclone, clonedisguise, clonedis, cdisguise, cdis, clonedisg, disgclone ] | Copy a disguise (or entity) and use it later. | `libsdisguises.seecmd.disguiseclone` |
| `/disguisemodify` | [ dmodify, dmod, disgmodify, modifydisguise, moddisguise, mdisguise ] | Modify your own disguise | `libsdisguises.seecmd.disguisemodify` |
| `/disguisemodifyentity` | [ dmodifyentity, dmodentity, disgmodentity, dismodentity, modifydisguiseentity, modifydisgentity, | Modify a disguise by right clicking them | `libsdisguises.seecmd.disguisemodifyentity` |
| `/disguisemodifyplayer` | [ dmodifyplayer, dmodplayer, disgmodifyplayer, dismodplayer, disgmodplayer, modifydisguiseplayer, | Modify the disguise of a 玩家 | `libsdisguises.seecmd.disguisemodifyplayer` |
| `/disguisemodifyradius` | [ dmodifyradius, dmodradius, disgmodradius, dismodradius, modifydisguiseradius, modifydisgradius, | Modify disguises in a radius | `libsdisguises.seecmd.disguisemodifyradius` |
| `/disguisemodifyselector` | [ dmodifyselector, dmodselector, disgmodselector, dismodselector, modifydisguiseselector, modifydisgselector, | Modify entity disguises via entity selector | `libsdisguises.seecmd.disguisemodifyselector` |
| `/savedisguise` | [ customdisguise, savedisg, customdisg, createdisguise, createdisg ] | Save a custom disguise to disguises.yml | `libsdisguises.seecmd.savedisguise` |


---

## <a id="litesignin"></a>LiteSignIn
* 檔案路徑: [`plugins/LiteSignIn-1.9.0.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/LiteSignIn-1.9.0.0.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/signin` | [litesignin] | Main 指令 of LiteSignIn. | `無` |


---

## <a id="luckperms"></a>LuckPerms
* 檔案路徑: [`plugins/LuckPerms-Bukkit-5.5.17.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/LuckPerms-Bukkit-5.5.17.jar)
* 功能概述: A 權限 plugin

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/luckperms` | [lp, perm, perms, permission, permissions] | 管理 權限 | `luckperms.admin` |


---

## <a id="maplockplus"></a>MapLockPlus
* 檔案路徑: [`plugins/maplockplus-1.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/maplockplus-1.1.jar)
* 功能概述: Plugin for locking maps from being copied

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> [anon|reload]` | [ml, lockmap] | Lock or unlock a map | `maplock.use` |


---

## <a id="minimotd"></a>MiniMOTD
* 檔案路徑: [`plugins/minimotd-paper-2.2.2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/minimotd-paper-2.2.2.jar)
* 功能概述: Use MiniMessage text formatting in the server list MOTD.

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="multiverse-core"></a>Multiverse-Core
* 檔案路徑: [`plugins/multiverse-core-5.5.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/multiverse-core-5.5.3.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="multiverse-netherportals"></a>Multiverse-NetherPortals
* 檔案路徑: [`plugins/multiverse-netherportals-5.0.4.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/multiverse-netherportals-5.0.4.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="mythicmobs"></a>MythicMobs
* 檔案路徑: [`plugins/MythicMobs-5.11.2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/MythicMobs-5.11.2.jar)
* 功能概述: The total solution for all things mob-related.

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/addpin` | - | quickly adds a pin | `無` |
| `/mythicmobs` | [mm] | MythicMobs base 指令 | `mythicmobs.admin` |
| `/mythicmobsmenu` | [mmmenu,mmm] | MythicMobs menu 指令 | `無` |
| `/pins` | [pin] | Easier 指令 for pins | `無` |
| `/spawnmob` | [spawnmythicmob,mspawn,msummon] | 生成點/出生點 a mob | `無` |


---

## <a id="placeholderapi"></a>PlaceholderAPI
* 檔案路徑: [`plugins/PlaceholderAPI-2.12.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/PlaceholderAPI-2.12.3.jar)
* 功能概述: An awesome placeholder provider!

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/placeholderapi` | ["papi"] | PlaceholderAPI 指令 | `placeholderapi.*` |


---

## <a id="playerkits2"></a>PlayerKits2
* 檔案路徑: [`plugins/PlayerKits2-1.21.2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/PlayerKits2-1.21.2.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/kit` | [kits,playerkits] | Main 指令 of PlayerKits2 | `無` |


---

## <a id="protocollib"></a>ProtocolLib
* 檔案路徑: [`plugins/ProtocolLib.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ProtocolLib.jar)
* 功能概述: Provides read/write access to the Minecraft protocol.

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> add|remove name [ID start]-[ID stop]` | [packet_filter] | Add or remove programmable filters to the packet listeners. | `protocol.admin` |
| `/<command> add|remove|names client|server [ID start]-[ID stop] [detailed]` | - | Add or remove a simple packet listener. | `protocol.admin` |
| `/<command> <protocol> <sender> <packet> [location]` | - | Logs hex representations of packets to a file or console | `protocol.admin` |
| `/<command> config|check|update|timings|listeners|version|dump` | - | Performs administrative tasks regarding ProtocolLib. | `protocol.admin` |


---

## <a id="quickshop-hikari"></a>QuickShop-Hikari
* 檔案路徑: [`plugins/QuickShop-Hikari-6.2.0.11.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/QuickShop-Hikari-6.2.0.11.jar)
* 功能概述: 箱子商店交易系統。玩家可利用箱子展示物品並自設售價，實現安全的離線自動化交易。

#### 商店建立說明：
1. **建立出售商店**：放好箱子，手持欲販售物品，面向箱子輸入 `/qs create <價格>`。
2. **切換買賣模式**：看向建立好的商店輸入 `/qs buy` 可切換為「收購模式」；輸入 `/qs sell` 可切換回「出售模式」。
3. **更改售價**：看向商店輸入 `/qs price <新價格>` 可直接修改該商品售價。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/qs buy` | - | 看向商店，將其模式切換為收購模式 (向他人收購該物品)。 | `quickshop.create` |
| `/qs create <價格>` | - | 看向箱子，將手持物品以指定單價註冊為箱子商店。 | `quickshop.create` |
| `/qs find <物品>` | - | 檢索一定範圍內有販售該物品的玩家商店。 | `quickshop.find` |
| `/qs price <價格>` | - | 看向商店，變更商品的單個交易價格。 | `quickshop.create` |
| `/qs sell` | - | 看向商店，將其模式切換為出售模式 (出售箱內物品給他人)。 | `quickshop.create` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/qs reload` | - | 重新載入商店配置文件並重新連接資料庫。 | `quickshop.reload` |


---

## <a id="residence"></a>Residence
* 檔案路徑: [`plugins/Residence6.0.2.4.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Residence6.0.2.4.jar)
* 功能概述: 三維領地圈地保護系統。提供玩家自行劃定保護區，防止方塊破壞、爆炸與容器未授權開啟。

#### 圈地操作指引：
1. **選取區域邊界**：手持木鋤（預設工具）進行兩點標記：
   * 朝向第一個角落方塊點擊 **滑鼠左鍵**，設定為 **點 1**。
   * 朝向對角線的另一個方塊點擊 **滑鼠右鍵**，設定為 **點 2**。
2. **擴展垂直範圍**：輸入 `/res select vert`，將選區垂直拉伸至最高與最低邊界（天空至基岩）。
3. **創建領地**：輸入 `/res create <領地名稱>`（如 `/res create base`）。系統將自動扣除對應的遊戲幣。
4. **變更權限 (Flags)**：
   * 使用 `/res set` 可開啟圖形化界面直接切換領地各項規則（如 `pvp`、`build`、`use`、`container`）。
   * 使用 `/res pset <領地名稱> <玩家> build true` 可單獨授權特定玩家於領地內建造。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/res create <領地名稱>` | - | 購買並將當前選定的三維空間註冊為個人領地。 | `residence.create` |
| `/res info [領地名稱]` | - | 查詢當前站立位置或指定領地的擁有者、尺寸及 Flag 狀態。 | `residence.select` |
| `/res list` | - | 列出您名下擁有的所有領地。 | `residence.select` |
| `/res pset <領地> <玩家> <權限Flag> <true/false/remove>` | - | 配置指定玩家在該領地內的個別操作權限。 | `residence.pset` |
| `/res remove <領地名稱>` | - | 註銷並刪除您擁有的指定領地（將退回部分資金）。 | `residence.create` |
| `/res select` | - | 顯示當前選取的區塊範圍大小與創建所需費用。 | `residence.select` |
| `/res select vert` | - | 將當前平面選區垂直延伸至天空頂部與基岩底部。 | `residence.select` |
| `/res set [領地] [權限Flag] [true/false]` | - | 開啟領地權限設定 GUI。或手動配置領地 Flag 規則（如 `pvp`、`build`、`use`、`container`）。 | `residence.set` |
| `/res tp <領地名稱>` | - | 傳送至指定領地的預設傳送點。 | `residence.tp` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/res admin` | - | 管理員超控模式。啟用後可無視保護規則對任意領地進行編輯或刪除。 | `residence.admin` |


---

## <a id="score"></a>SCore
* 檔案路徑: [`plugins/SCore-5.26.7.5.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SCore-5.26.7.5.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/<command> [ reload | inspect-loop ]` | - | score 指令 | `score.*` |


---

## <a id="sethome"></a>SetHome
* 檔案路徑: [`plugins/SetHome_GUI-2.1.4.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SetHome_GUI-2.1.4.jar)

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/home` | [homegui, sethomegui] | Open the home menu. | `無` |


---

## <a id="shopkeepers"></a>Shopkeepers
* 檔案路徑: [`plugins/Shopkeepers-2.27.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Shopkeepers-2.27.0.jar)
* 功能概述: Custom villager shopkeepers

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `Unknown command! Try /<command> help` | [shopkeepers] | Base for all shopkeeper 指令. | `shopkeeper.help` |


---

## <a id="simple_rtp"></a>Simple_RTP
* 檔案路徑: [`plugins/Simple_RTP-1.0.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Simple_RTP-1.0.3.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/rtp` | - | 傳送 to a random spot. | `simplertp.*` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/rtpreload` | - | 重新載入 Simple RTP. | `無` |


---

## <a id="skbee"></a>SkBee
* 檔案路徑: [`plugins/SkBee-3.25.2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SkBee-3.25.2.jar)
* 功能概述: A simple Skript addon to help customize your server to the fullest.

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="skinsrestorer"></a>SkinsRestorer
* 檔案路徑: [`plugins/SkinsRestorer.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SkinsRestorer.jar)
* 功能概述: 玩家皮膚切換工具。支援複製正版玩家外觀或使用圖片網址直鏈套用自訂皮膚。

#### 操作指引：
1. **套用正版外觀**：輸入 `/skin <正版玩家帳號>` (如 `/skin Steve`)。
2. **套用自訂外觀**：上傳皮膚 .png 至圖床後，輸入 `/skin url <直鏈網址>`。
3. **還原默認皮膚**：輸入 `/skin clear`。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/skin <正版ID>` | - | 複製並套用指定正版玩家的皮膚外觀。 | `skinsrestorer.command.skin` |
| `/skin clear` | - | 清除當前套用的皮膚，還原為原本的默認皮膚。 | `skinsrestorer.command.skin.clear` |
| `/skin url <.png直鏈>` | - | 使用特定圖片網址為自己替換外形。 | `skinsrestorer.command.skin.url` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/sr reload` | - | 管理員指令：重新載入皮膚緩存與設定檔。 | `skinsrestorer.command.admin` |
| `/sr set <玩家> <正版ID>` | - | 管理員指令：強制將指定玩家的皮膚設定為該正版ID的皮膚。 | `skinsrestorer.command.admin` |


---

## <a id="skript"></a>Skript
* 檔案路徑: [`plugins/Skript-2.16.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Skript-2.16.0.jar)
* 功能概述: Customize Minecraft's mechanics with simple scripts written in plain English sentences.

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/skript help` | [sk] | Skript's main 指令. Type '/skript help' for more information. | `skript.admin` |


---

## <a id="slimefun"></a>Slimefun
* 檔案路徑: [`plugins/SlimefunCore4-2708.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SlimefunCore4-2708.jar)
* 功能概述: 黏液科技核心。在不安裝伺服器模組的前提下，提供機器建造、電力自動化、核能、魔法及進階裝備系統。

#### 研發操作說明：
1. **開啟導覽手冊**：輸入 `/sf guide` 開啟或取得 **Slimefun 導覽書**。
2. **科技解鎖**：點擊手冊內的科技分類（如基礎機器、武器等）。研發配方需消耗玩家對應的經驗值等級。
3. **搭建多方塊結構機器**：Slimefun 機器由特定原版方塊按指定結構堆疊而成（如研磨機由發射器、柵欄、金砧堆疊）。
   * 於發射器中放入原料，右鍵點擊頂部的金砧即可執行研磨加工。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/sf guide` | /slimefun guide | 開啟或取得 Slimefun 導覽書 GUI，用於研發與查閱配方。 | `slimefun.command.guide` |
| `/sf search <關鍵字>` | - | 於導覽手冊中檢索包含關鍵字的物品或合成配方。 | `slimefun.command.search` |
| `/sf stats [玩家]` | - | 查詢自身或指定玩家的科技研發進度與解鎖百分比。 | `slimefun.command.stats` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/sf cheat` | - | 管理員創造模式。開啟後可直接無視限制獲取任意 Slimefun 物品。 | `slimefun.cheat` |
| `/sf give <玩家> <物品ID> [數量]` | - | 給予指定玩家特定的 Slimefun 物品。 | `slimefun.command.give` |
| `/sf reload` | - | 重新載入 Slimefun 核心與附屬插件之設定檔。 | `slimefun.command.reload` |
| `/sf research <玩家> <all/解鎖項目>` | - | 強制幫特定玩家解鎖指定或全部科技配方。 | `slimefun.command.research` |


---

## <a id="slimefuntranslation"></a>SlimefunTranslation
* 檔案路徑: [`plugins/SF_ SlimefunTranslation-MODIFIED v0.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SF_ SlimefunTranslation-MODIFIED v0.1.jar)
* 功能概述: A Slimefun Addon that translates items without actually modifying the

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/sftranslation` | - | SlimefunTranslation 指令 | `sftranslation.command.id` |


---

## <a id="spherelib"></a>SphereLib
* 檔案路徑: [`plugins/SphereLib-0.6.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SphereLib-0.6.3.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="superiorskyblock2"></a>SuperiorSkyblock2
* 檔案路徑: [`plugins/SuperiorSkyblock2-2026.2.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/SuperiorSkyblock2-2026.2.jar)
* 功能概述: 高性能空島生存模組。管理島嶼建立、升級、日常任務、島嶼資金及成員操作權限。

#### 島嶼操作說明：
1. **建立空島**：輸入 `/is`，選取欲使用的島嶼模版後，系統將自動生成並傳送至該空島。
2. **組隊邀請**：輸入 `/is invite <玩家>` 邀請他人加入您的空島，對方接受後將共用同一島嶼空間。
3. **計算島嶼價值**：輸入 `/is level`。系統將掃描島嶼上所有方塊的價值以更新島嶼等級評分。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/is (或 /island)` | /is | 開啟空島的核心 GUI 主面板或進行空島創建。 | `superiorskyblock.island.go` |
| `/is bank` | - | 開啟空島共同銀行，可存入或取出島嶼公用金幣與經驗值。 | `superiorskyblock.island.bank` |
| `/is home` | - | 傳送回自己空島的起點傳送門位置。 | `superiorskyblock.island.go` |
| `/is invite <玩家>` | - | 邀請一名玩家加入您的空島團隊（隊友會失去他原本的島嶼）。 | `superiorskyblock.island.invite` |
| `/is leave` | - | 主動退出目前加入的空島小組。 | `superiorskyblock.island.leave` |
| `/is level` | - | 重新計算並查看您目前島嶼的價值與等級評分。 | `superiorskyblock.island.level` |
| `/is lock` | - | 鎖定或解鎖島嶼。鎖定後非島嶼成員將無法進入或傳送到該島嶼。 | `superiorskyblock.island.lock` |
| `/is sethome` | - | 變更並將目前的站立點設為島嶼的主傳送點。 | `superiorskyblock.island.sethome` |
| `/is top` | - | 查看伺服器中島嶼等級最高的排行榜單。 | `superiorskyblock.island.top` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/is admin reload` | - | 管理員指令：重載空島設定與任務檔。 | `superiorskyblock.admin` |


---

## <a id="tab"></a>TAB
* 檔案路徑: [`plugins/TAB v6.1.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/TAB v6.1.0.jar)
* 功能概述: An all-in-one solution that works

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/tab` | - | Plugin's main 指令 | `tab.admin` |


---

## <a id="theosiseconomy"></a>TheosisEconomy
* 檔案路徑: [`plugins/TheosisEconomy-1.46.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/TheosisEconomy-1.46.jar)

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/balance` | - | See your own or another 玩家's 餘額. | `theosiseconomy.command.balance` |
| `/balancetop` | - | See a list of all 玩家' balances from richest to poorest, and the combined total 餘額 of all 玩家. | `theosiseconomy.command.balancetop` |
| `/economy` | - | 管理 the 經濟系統. | `theosiseconomy.command.economy` |
| `/pay` | - | Pay another 玩家 a specified amount of 金錢. | `theosiseconomy.command.pay` |
| `/paytoggle` | - | 切換 whether you want other 玩家 to be able to pay you 金錢 with the "/pay" 指令. | `theosiseconomy.command.paytoggle` |


---

## <a id="townsandnations"></a>TownsAndNations
* 檔案路徑: [`plugins/TownsAndNations-1.0.3.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/TownsAndNations-1.0.3.jar)
* 功能概述: 城鎮與國家防護系統。支援玩家創建市鎮、劃分轄區、設定稅收、加入國家結盟及參與防禦戰役。

#### 建立與營運說明：
1. **建立城鎮**：輸入 `/tan create town <城鎮名稱>`。扣除開辦資金後，您將自動成為鎮長。
2. **營運資金存取**：城鎮每日會扣除固定維護費。請使用 `/tan deposit <金額>` 將金錢存入城鎮公庫，以防城鎮因欠費解散。
3. **擴張城鎮領土**：站在欲劃歸城鎮的荒野區塊（Chunk），輸入 `/tan claim` 以將該區塊圈定為城鎮領土。
4. **市民招募**：輸入 `/tan invite <玩家>` 邀請玩家加入城鎮。

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/tan claim` | - | 將當前站立的 Chunk（16x16 區塊）劃定為城鎮所屬領地。 | `townsandnations.town.claim` |
| `/tan create town <城鎮名稱>` | - | 建立新城鎮並取得該城鎮的鎮長權限。 | `townsandnations.town.create` |
| `/tan deposit <金額>` | - | 存入金錢至城鎮公庫，以維持城鎮每日運作。 | `townsandnations.town.use` |
| `/tan invite <玩家>` | - | 邀請指定玩家加入您的城鎮團隊。 | `townsandnations.town.invite` |
| `/tan leave` | - | 主動退出目前所屬的城鎮。 | `townsandnations.town.use` |
| `/tan town` | - | 開啟城鎮管理 GUI，查詢資金、成員狀態、區塊配置與稅收。 | `townsandnations.town.use` |
| `/tan unclaim` | - | 解圈並放棄當前站立的城鎮 Chunk 領地。 | `townsandnations.town.claim` |
| `/tan withdraw <金額>` | - | 從城鎮公庫中提取金錢（限鎮長與具備提款權限之管理階層）。 | `townsandnations.town.withdraw` |

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/tan admin` | - | 管理員維護指令。可強制解散城鎮、沒收領地或重載設定檔。 | `townsandnations.admin` |


---

## <a id="tpagui"></a>TpaGui
* 檔案路徑: [`plugins/TpaGui.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/TpaGui.jar)

### 玩家權限指令 (User Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `§c用法: /<command>` | [tpag, tgui] | 打开传送请求GUI菜单 | `tpagui.use` |


---

## <a id="vault"></a>Vault
* 檔案路徑: [`plugins/Vault.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Vault.jar)
* 功能概述: Vault is a 權限 & 經濟系統 API to allow plugins to more easily hook into these systems without needing to hook each individual system themselves.

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `|` | - | Converts all data in economy1 and dumps it into economy2 | `vault.admin` |
| `|` | - | 顯示 information about Vault | `vault.admin` |


---

## <a id="veinminer"></a>Veinminer
* 檔案路徑: [`plugins/veinminer-paper-2.6.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/veinminer-paper-2.6.0.jar)
* 功能概述: Mine the whole vein at the same time with a single block break

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="viabackwards"></a>ViaBackwards
* 檔案路徑: [`plugins/ViaBackwards-5.11.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ViaBackwards-5.11.0.jar)
* 功能概述: Allows the connection of older clients to newer server versions for Minecraft servers.

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="viaversion"></a>ViaVersion
* 檔案路徑: [`plugins/ViaVersion-5.11.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ViaVersion-5.11.0.jar)
* 功能概述: Allows the connection of newer clients to older server versions for Minecraft servers.

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/viaversion` | [ viaver, vvbukkit ] | 顯示 ViaVersion Version and more. | `viaversion.command` |


---

## <a id="voidworld"></a>VoidWorld
* 檔案路徑: [`plugins/VoidWorld-1.0.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/VoidWorld-1.0.0.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="worldedit"></a>WorldEdit
* 檔案路徑: [`plugins/worldedit-bukkit-7.4.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/worldedit-bukkit-7.4.1.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="worldguard"></a>WorldGuard
* 檔案路徑: [`plugins/worldguard-bukkit-7.0.16.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/worldguard-bukkit-7.0.16.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="znpcsplus"></a>ZNPCsPlus
* 檔案路徑: [`plugins/ZNPCsPlus-2.1.0-SNAPSHOT.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/ZNPCsPlus-2.1.0-SNAPSHOT.jar)

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/npc` | - | - | `znpcsplus.command.npc` |


---

## <a id="eshulkerbox"></a>eShulkerBox
* 檔案路徑: [`plugins/eShulkerBox-0.8.5.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/eShulkerBox-0.8.5.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="floodgate"></a>floodgate
* 檔案路徑: [`plugins/floodgate-spigot.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/floodgate-spigot.jar)
* 功能概述: Allows Bedrock 玩家 to join Java edition servers while keeping the server in online mode

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="nightcore"></a>nightcore
* 檔案路徑: [`plugins/nightcore-2.14.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/nightcore-2.14.0.jar)
* 功能概述: Plugin core

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="packetevents"></a>packetevents
* 檔案路徑: [`plugins/packetevents-spigot-2.13.0.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/packetevents-spigot-2.13.0.jar)

> *該插件為函式庫或未註冊任何指令與權限。*


---

## <a id="playerhead"></a>playerHead
* 檔案路徑: [`plugins/playerHead-1.1.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/playerHead-1.1.jar)

### 管理員權限指令 (Admin/OP Commands)
| 指令格式與用法 | 別名 (Aliases) | 功能描述 | 權限節點 (Permission Node) |
| :--- | :--- | :--- | :--- |
| `/playerhead <username>` | - | Gives the head of the specified Minecraft username. | `playerhead.give` |


---

## <a id="qsaddon-discordsrv"></a>qsaddon-discordsrv
* 檔案路徑: [`plugins/Addon-DiscordSRV-6.2.0.11.jar`](file:///C:/Users/smart/Downloads/測試企鵝/20260720/plugins/Addon-DiscordSRV-6.2.0.11.jar)

### 權限節點清單 (Permission Nodes)
| 權限節點 | 說明 | 預設狀態 (Default) |
| :--- | :--- | :--- |
| `quickshopaddon.discord.use` | Allows 玩家 to use discord 指令 | `True` |


---
