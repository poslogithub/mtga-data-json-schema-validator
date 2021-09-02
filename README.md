# mtga-data-json-schema-validator
 Validator for data_*.mtga files.

## Usage
`py mtga-data-json-schema-validator [mtga_data_dir] [schema_dir]`

## Default values

* mtga_data_dir
  * C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Data
* schema_dir
  * .\json-schema
  
## Known issues

* Cannot validate `data_altPrintings_*.mtga` because it has invalid comments like `/*missing en-US translation for LocID: 2999*/`
