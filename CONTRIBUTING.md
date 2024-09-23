# Contributing to the Economic Model Papers Repository

We are thrilled that you're interested in contributing! Your efforts will help advance economic research and education. To ensure a smooth collaboration process, please follow these guidelines.

## **Table of Contents**

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Submitting a New Paper](#submitting-a-new-paper)
  - [Improving Existing Papers](#improving-existing-papers)
  - [Contributing to Common Resources](#contributing-to-common-resources)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

---

## **Getting Started**

1. **Fork the Repository**

   - Click the "Fork" button at the top right corner of this page to create a copy of this repository on your GitHub account.

2. **Clone Your Fork**

   - Clone the repository to your local machine using:

     ```bash
     git clone https://github.com/your-username/economic-model-papers.git
     ```

3. **Set Upstream Remote**

   - Set the upstream remote to keep your fork synchronized with the original repository:

     ```bash
     git remote add upstream https://github.com/original-author/economic-model-papers.git
     ```

## **How to Contribute**

### **Submitting a New Paper**

1. **Create a New Branch**

   - Create a descriptive branch for your paper:

     ```bash
     git checkout -b add-your-paper-title
     ```

2. **Use the Template**

   - Navigate to the `future-paper-template/` directory.
   - Copy the template folder to the `papers/` directory (coordinate with maintainers to avoid conflicts):

     ```bash
     cp -r future-paper-template/ papers/your-paper-title/
     ```

   - Rename files appropriately and begin adding your content.

3. **Add Your Content**

   - Write your paper in Markdown format using `paper-template.md`.
   - Include any appendices, data files, code, and figures as needed.
   - Ensure all files are properly organized within your paper's directory.

4. **Document Your Work**

   - Update the `README.md` in your paper's directory with an overview and instructions for replication.

### **Improving Existing Papers**

- **Open an Issue**

  - Before making changes, open an issue to discuss your proposed improvements.

- **Make Changes**

  - Create a new branch:

    ```bash
    git checkout -b improve-paper-title
    ```

  - Make your edits, ensuring to follow the repository's formatting and style guidelines.

### **Contributing to Common Resources**

- **Adding Code Snippets**

  - Place new code snippets in `common-resources/code-snippets/`.
  - Include a brief description at the top of each file explaining its purpose.

- **Adding Datasets**

  - Add datasets to `common-resources/data/`.
  - Provide a `README.md` in the data directory explaining the source, format, and any processing steps.

- **Updating References**

  - Update `common-resources/references/economic-research-papers.md` with relevant literature.

## **Pull Request Process**

1. **Commit Your Changes**

   - Write clear and descriptive commit messages.

2. **Push to Your Fork**

   - Push your branch to your forked repository:

     ```bash
     git push origin your-branch-name
     ```

3. **Submit a Pull Request**

   - Go to the original repository and submit a pull request.
   - Provide a clear title and description of your changes.

4. **Review and Discussion**

   - Collaborate with maintainers and other contributors to review your changes.
   - Be responsive to feedback and make revisions as necessary.

## **Code of Conduct**

- **Respectful Communication**

  - Be courteous and respectful in all interactions.
  - Critique ideas, not people.

- **Inclusivity**

  - Encourage participation from a diverse range of contributors.

- **Compliance**

  - Adhere to all applicable laws and regulations.

## **License**

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for your interest in contributing! Your efforts help make this repository a valuable resource for the community.
