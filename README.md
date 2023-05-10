# Module Firmware Version

## OS
| | |
|:---|:---|
| e103 | **v1.3.2** |
| e230 | **v1.3.2** |

## Bootloader
| | |
|:---|:---|
| e103 | v1.0.1 |
| e230 | v1.0.0 |

## Module
| | |
|:---|:---|
| Battery | **v1.1.0** |
| Button | v1.0.1 |
| Dial | v1.0.5 |
| Display | **v1.3.2** |
| Environment | v1.0.3 |
| Imu | v1.1.4 |
| Joystick | v1.1.2 |
| Led | v1.0.1 |
| Motor | **v1.2.3** |
| Speaker | v1.2.2 |
| Tof | **v1.1.5** |
| Network app | **v1.1.5** |
| Network sub | **v4.4.2** |
| Network ota | **v1.1.0** |
| Camera app | **v1.0.1** |
| Camera sub | **v1.0.1** |

# Changelog

## Feature

### OS
1. Hardfault 발생 시, bootloader로 이동하지 않음

### Battery
1. 충전 시, 상태 led 점등

### Display
1. Battery 모듈 PnP 동작 변경

### Motor
1. 최단경로 이동 모드 추가

## Hotfix

### Network sub
1. 유저 코드 실행 시, 이전 모듈 데이터가 남아있는 오류 수정

### Network ota
1. BLE 통신 방식 추가

## Patch

### Network sub
1. OTA 업로더 UI 수정
