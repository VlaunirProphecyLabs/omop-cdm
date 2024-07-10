from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from l42_omop531etlsynthea.udfs.UDFs import *

def concept_ancestor(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"`{Config.catalog_name}`.`{Config.database_name}`.`concept_ancestor`")
