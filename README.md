# Distributed Data Parallel Computing with Spark

This lab is an **introduction to the Apache Spark framework** for Data Parallel processing on distributed environments. We will be using it in the context of the Python programming language via the `pyspark` module.

---

## 🛠️ Setup Requirements and Installation

### Docker-based Installation

Please read the setup guide previously provided. Now we need to update the Docker Compose file to include the volumes for this lab.

You may either simply copy the Docker files of the previous project into this one (which will create new images that take up extra space on your disk) or update the existing container mappings. 

For the latter option, find your `docker-spark-env` folder and edit the `docker-compose.yml` file to add the new volumes:

```yaml
services:
  spark:
    # ...
    volumes:
      # ...
      - PATH_TO_THIS_PROJECT/apps:/apps/lab01
      - PATH_TO_THIS_PROJECT/data:/data/lab01
      
  jupyter:
    # ...
    volumes:
      # ...
      - PATH_TO_THIS_PROJECT/notebooks:/workspace/lab01
      - PATH_TO_THIS_PROJECT/data:/data/lab01
```

Where `PATH_TO_THIS_PROJECT` is either:
- The absolute path to the root folder of this project.
- The relative path from `docker-spark-env` to the root folder of this project.

Now, let's rebuild and run the environment:

```bash
cd /PATH_TO/docker-spark-env
docker compose up -d --scale spark-worker=3 --build
```

### Local Installation

If you prefer, you can also set up a local Python virtual environment that includes the `pyspark` module.

You have to install:
* A **Python distribution** (> 3.7)
* A **Python IDE** (e.g., VS Code or PyCharm)
* **Java Development Kit (JDK)** version 17 (highly recommended for compatibility)
* **PySpark** via pip:

```bash
pip install pyspark
```

---

## 📝 Word Count Example

Word counting is a fundamental text analysis process that calculates the total number of words in a given text. It is widely used for monitoring document length and analyzing word frequency. It is also the standard example for distributed data processing.

The process typically involves reading the input text, splitting it into words, and counting how many times each word appears.

### Example Case
* **Input Text:** `"Big data means big opportunities with big challenges."`
* **Expected Output:**
  ```text
  big → 3
  data → 1
  means → 1
  opportunities → 1
  with → 1
  challenges → 1
  ```

### Provided Implementations
Please test and review the following implementations inside the project:

| File Path | Description |
| :--- | :--- |
| `notebooks/word_count.ipynb` | Interactive Jupyter Notebook containing the sequential Python implementation, the low-level **Spark RDD API**, and the high-level **Spark SQL/DataFrame API**. |

---

## 💻 Work To Do

Analyze the code on the `notebooks/flights.ipynb` Jupyter notebook. Implement functions to compute:
* 📊 **The number of flights per route**
* 🏆 **The route with the highest number of flights**
* ⏱️ **The average duration of flights per route**

---

## 📚 Documentation

* [Apache Spark Official Documentation](https://apache.org)
* [Spark RDD Programming Guide](https://apache.orgrdd-programming-guide.html)
* [Spark SQL Programming Guide](https://apache.orgsql-programming-guide.html)
* [TutorialsPoint: Spark SQL Tutorial](https://tutorialspoint.com)
