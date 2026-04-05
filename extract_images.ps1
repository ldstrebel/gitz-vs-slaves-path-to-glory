# extract_images.ps1
$inputFile = "WH P2G/Path to Glory.md"
$outputFile = "WH P2G/Path to Glory (Clean).md"
$imageDir = "attached_assets/images"

if (!(Test-Path $imageDir)) { New-Item -ItemType Directory $imageDir }

$reader = [System.IO.File]::OpenText($inputFile)
$writer = [System.IO.StreamWriter]::new($outputFile)

while (($line = $reader.ReadLine()) -ne $null) {
    if ($line -match '\[image(\d+)\]: <data:image/png;base64,(.*)>') {
        $imgNum = $matches[1]
        $base64 = $matches[2]
        $imgFile = "$imageDir/ptg_p2g_img_$imgNum.png"
        
        # Save base64 to file
        try {
            $bytes = [System.Convert]::FromBase64String($base64)
            [System.IO.File]::WriteAllBytes($imgFile, $bytes)
            $writer.WriteLine("[image$imgNum]: ../attached_assets/images/ptg_p2g_img_$imgNum.png")
            Write-Host "Extracted image $imgNum to $imgFile"
        } catch {
            Write-Host "Failed to extract image $imgNum : $($_.Exception.Message)"
            $writer.WriteLine($line) # Keep original if failed
        }
    } else {
        $writer.WriteLine($line)
    }
}

$reader.Close()
$writer.Close()
