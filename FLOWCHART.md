# Flowchart & Process Logic Documentation
## Physics Experiment Helper (CBSE Class XII - Subject Code 083)

---

## 1. System Master Flowchart

The following flowchart models the exact operational lifecycle and decision logic represented in the CBSE project documentation (corresponding to `image4.jpeg` from the project report):

```mermaid
flowchart TD
    Start([Start]) --> ImportLib[Import Standard Libraries\ncsv, math, typing, dataclasses]
    ImportLib --> DefFunc[Define Core Experiment Classes\n& Factory Registry]
    DefFunc --> MainLoop{Main Loop:\nWhile True}

    MainLoop --> DisplayMenu[Display 12 Main Menu Options]
    DisplayMenu --> UserPrompt[/Prompt User for Task Number: 1 to 12/]
    UserPrompt --> ValidateTask{Validate Task Input}

    %% Invalid Task
    ValidateTask -->|Invalid Number / String| PrintInvalid[Print 'Invalid input. Please enter 1-12']
    PrintInvalid --> MainLoop

    %% Exit Task
    ValidateTask -->|Choice == 12| PrintExit[Print 'Exiting application...']
    PrintExit --> Terminate([End / Terminate])

    %% Experiment Task (1-10)
    ValidateTask -->|Choice in 1..10| PromptExpInputs[/Prompt User for Experiment Readings/]
    PromptExpInputs --> ValidateExpInputs{Validate Physical\nBoundaries}
    ValidateExpInputs -->|Invalid / Out of Bounds| PrintExpError[Print 'Invalid input. Re-prompt']
    PrintExpError --> PromptExpInputs
    ValidateExpInputs -->|Valid Inputs| RunCalc[Call Experiment.calculate\nExecute Formulae & Error Propagation]
    RunCalc --> DisplayResults[/Print Formatted Calculation Results & Warnings/]
    DisplayResults --> PromptStore{Store Data in\nDatabase?}
    PromptStore -->|Yes| SaveCSV[Append Record to CSV File in data/ directory\nWrite Headers if New File]
    SaveCSV --> MainLoop
    PromptStore -->|No| MainLoop

    %% Retrieval Task (11)
    ValidateTask -->|Choice == 11| PromptRetrieval[/Select Experiment Database 1-10/]
    PromptRetrieval --> ValidateRetChoice{Valid Experiment\nNumber?}
    ValidateRetChoice -->|Invalid| PrintRetError[Print 'Please enter a valid task number']
    PrintRetError --> MainLoop
    ValidateRetChoice -->|Valid| CheckFile{Check if CSV File\nExists & Has Data}
    CheckFile -->|File Found & Non-Empty| ReadRecords[Read CSV Records via CSVRepository]
    ReadRecords --> FormatTable[Generate Aligned ASCII Table & Compute Stats]
    FormatTable --> PrintTable[/Display Formatted Table & Statistics/]
    PrintTable --> MainLoop
    CheckFile -->|File Not Found / Empty| PrintFileNotFound[Print 'File not found or contains no records']
    PrintFileNotFound --> MainLoop
```

---

## 2. Sub-Process Flowcharts

### 2.1 Experiment Calculation & Error Propagation Sub-Flow

```mermaid
flowchart TD
    subgraph Calc_Engine ["Calculation Engine Sub-Process"]
        Inp[Receive Validated Input Parameters] --> CheckZeros{Check for Zero Divisors\n& Physical Bounds}
        CheckZeros -->|Division by Zero| RetZeroErr[Return CalculationResult with error_message]
        CheckZeros -->|Physical Impossibility| RetBoundErr[Return Physical Violation Warning]
        CheckZeros -->|Valid| MathExec[Execute Primary Formula]
        MathExec --> ErrCalc[Execute Fractional & Absolute Error Propagation]
        ErrCalc --> WarnCheck{Check Value against\nStandard Physical Benchmarks}
        WarnCheck -->|Noticeable Deviation| AddWarn[Append Domain Warning to Result]
        WarnCheck -->|Normal Range| PackResult[Pack Values, Errors, Warnings into CalculationResult]
        AddWarn --> PackResult
        PackResult --> ReturnRes[Return CalculationResult to UI]
    end
```

### 2.2 CSV Persistence & Schema Enforcement Sub-Flow

```mermaid
flowchart TD
    subgraph Storage_Engine ["Storage Sub-Process"]
        SaveReq[Receive Row Data & Header Specification] --> ResolvePath[Resolve Destination Path in data/ directory]
        ResolvePath --> CheckExists{Does File Exist\n& Have Size > 0?}
        CheckExists -->|No / Empty| CreateWithHeader[Open File in Append Mode\nWrite Header Row]
        CheckExists -->|Yes| OpenAppend[Open File in Append Mode]
        CreateWithHeader --> WriteData[Write Formatted Row Data]
        OpenAppend --> WriteData
        WriteData --> FlushClose[Flush Buffer & Close File]
        FlushClose --> RetSuccess[Return Success Status to Caller]
    end
```

---

## 3. CBSE Class XII Control Flow Table

| Step | State | Input | Condition / Validation | Transition |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `INIT` | System boot | Load standard libraries & configuration | Move to `MENU_DISPLAY` |
| **02** | `MENU_DISPLAY` | None | None | Prompt user choice (1–12) |
| **03** | `MENU_SELECT` | Integer `exp_no` | `1 <= exp_no <= 12` | If 1–10: `EXP_PROMPT`; If 11: `RETRIEVE_PROMPT`; If 12: `EXIT`; Else: error |
| **04** | `EXP_PROMPT` | Float/Int measurements | Physical constraints (e.g. $L > 0$, $D > x$) | If valid: `CALCULATE`; Else: re-prompt |
| **05** | `CALCULATE` | Valid inputs | Formula evaluated, error propagated | Display results & move to `STORE_PROMPT` |
| **06** | `STORE_PROMPT`| String (`yes`/`no`) | Case-insensitive boolean check | If `yes`: `CSV_WRITE`; If `no`: `MENU_DISPLAY` |
| **07** | `CSV_WRITE` | Row data | File presence check | Append record, display confirmation, move to `MENU_DISPLAY` |
| **08** | `RETRIEVE` | Integer (1–10) | File existence check | Render ASCII table and summary stats, return to `MENU_DISPLAY` |
| **09** | `EXIT` | User choice 12 | None | Print goodbye and terminate process |
