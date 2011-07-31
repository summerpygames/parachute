runningLoop = 3
selectedLog = 1
pygame.draw.rect(screen, (000, 000, 000), (((foundLogs[selectedLog][1]-1)*50), ((foundLogs[selectedLog][2]-1)*50), (foundLogs[selectedLogs][3]*50), 50), width = 1): return Rect
def outlineLog(selectedLog, foundLogs)
    pygame.draw.rect(screen, (000, 000, 000), (((foundLogs[selectedLog][1]-1)*50), ((foundLogs[selectedLog][2]-1)*50), (foundLogs[selectedLogs][3]*50), 50), width = 1): return Rect

while runningLoop == 3
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if selectedLog <= 1:
                    selectedLog = len(foundLogs)
                else:
                    selectedLog -= 1
                outlineLog(selectedLog, foundLogs)
            if event.key == pygame.K_RIGHT:
                if selectedLog >= len(foundLogs):
                    selectedLog = 1
                else:
                    selectedLog += 1
                outlineLog(selectedLog, foundLogs)

                    
