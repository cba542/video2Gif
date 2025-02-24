# Video to GIF Converter

一個簡單但功能強大的視頻轉 GIF 工具，可以自定義輸出的幀率、大小和幀數，幫助你創建最佳效果的 GIF 動畫。

## 功能特點

- 支持多種視頻格式轉換
- 可調整輸出 GIF 的大小
- 可控制輸出的幀率和總幀數
- 支持幀間隔採樣，減小文件體積

## 使用方法

```python
video_to_gif("input.mp4", "output.gif", fps=12, scale=0.5, max_frames=80, frame_skip=1)
```

### 高品質動畫
```python
video_to_gif("input.mp4", "output.gif", fps=15, scale=0.6, max_frames=100, frame_skip=0)
```

### 小文件體積
```python
video_to_gif("input.mp4", "output.gif", fps=10, scale=0.4, max_frames=60, frame_skip=2)
```

## 參數說明

### fps (幀率)
- 說明：每秒顯示的幀數
- 建議值：12-15
- 範圍：1-30
- 注意事項：
  - 較高的 fps 會產生更流暢的動畫，但文件體積更大
  - 較低的 fps 可以減小文件體積，但可能不夠流暢
  - 一般 GIF 使用 12-15 fps 就足夠流暢

### scale (縮放比例)
- 說明：輸出 GIF 相對於原視頻的尺寸比例
- 建議值：0.5 (縮小到原視頻的一半)
- 範圍：0.1-1.0
- 注意事項：
  - 較小的 scale 可以顯著減少文件大小
  - 建議根據原視頻分辨率來調整，通常 0.4-0.6 效果較好

### max_frames (最大幀數)
- 說明：限制 GIF 的最大幀數
- 建議值：60-100
- 範圍：10-300
- 注意事項：
  - 幀數越多，文件越大
  - 建議根據原視頻長度來調整
  - 一般 60-100 幀足以展示主要內容

### frame_skip (跳幀間隔)
- 說明：每隔多少幀取一幀
- 建議值：1-2
- 範圍：0-10
- 注意事項：
  - 0 表示不跳幀
  - 1 表示每隔一幀取一幀（即取偶數幀）
  - 較大的值可以減小文件體積，但可能造成動畫不夠流暢

## 最佳實踐建議

### 一般用途

## 注意事項

- 輸出文件大小與 fps、scale、max_frames 三個參數密切相關
- 建議先用默認參數測試，再根據需求調整參數
- 如果輸出文件過大，可以：
  1. 降低 fps
  2. 減小 scale
  3. 增加 frame_skip
  4. 減少 max_frames

  ### 一般用途
    video_to_gif("input.mp4", "output.gif", fps=12, scale=0.5, max_frames=80, frame_skip=1)

  ### 高品質動畫
    video_to_gif("input.mp4", "output.gif", fps=15, scale=0.6, max_frames=100, frame_skip=0)

  ### 小文件體積
    video_to_gif("input.mp4", "output.gif", fps=10, scale=0.4, max_frames=60, frame_skip=2)
