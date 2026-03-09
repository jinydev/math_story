param(
    [Parameter(Mandatory=$true)]
    [string]$base_dir
)

$md_dir = Join-Path $base_dir "md"

$chapters = @(
    @{ title="00_intro"; start=0; end=23 },
    @{ title="01_class1"; start=24; end=49 },
    @{ title="02_class2"; start=50; end=77 },
    @{ title="03_class3"; start=78; end=97 },
    @{ title="04_class4"; start=98; end=121 },
    @{ title="05_class5"; start=122; end=137 },
    @{ title="06_class6"; start=138; end=164 },
    @{ title="07_class7"; start=165; end=185 },
    @{ title="08_epilogue"; start=186; end=187 }
)

foreach ($c in $chapters) {
    $chapter_title = $c.title
    $start_idx = $c.start
    $end_idx = $c.end
    
    $output_path = Join-Path $base_dir "$chapter_title.md"
    $combined_content = @()
    
    for ($i = $start_idx; $i -le $end_idx; $i++) {
        $filename = "{0:D4}.md" -f $i
        $filepath = Join-Path $md_dir $filename
        
        if (Test-Path $filepath) {
            $content = Get-Content -Path $filepath -Raw -Encoding UTF8
            if ($null -ne $content) {
                # Fix image paths. Regex to replace absolute paths to ./img/ format
                $content = [System.Text.RegularExpressions.Regex]::Replace($content, '!\[([^\]]*)\]\((?:[^)]*?/img/)([^)]+)\)', '![$1](./img/$2)')
                if (-not [string]::IsNullOrWhiteSpace($content)) {
                    $combined_content += $content.Trim()
                }
            }
        }
    }
    
    $final_text = $combined_content -join "`r`n`r`n"
    if ([string]::IsNullOrWhiteSpace($final_text)) {
        $final_text = "`r`n"
    }
    
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [IO.File]::WriteAllText($output_path, $final_text, $utf8NoBom)
    
    Write-Host "Created $chapter_title.md with $($combined_content.Count) files joined."
}

Write-Host "All chapters successfully merged."
