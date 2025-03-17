document.addEventListener("DOMContentLoaded", function () {
    // 🔹 ADD STUDENT FUNCTIONALITY (already fixed)
    let addForm = document.getElementById("addStudentForm");
    if (addForm) {
        addForm.addEventListener("submit", function (e) {
            e.preventDefault();
            
            let formData = new FormData();
            formData.append("name", document.getElementById("name").value);
            formData.append("id", document.getElementById("studentId").value);
            formData.append("class", document.getElementById("class").value);
            formData.append("image", document.getElementById("studentImage").files[0]);

            axios.post("/add_student", formData, {
                headers: { "Content-Type": "multipart/form-data" }
            })
            .then(response => {
                alert(response.data.message);
                addForm.reset();
            })
            .catch(error => {
                console.error("❌ Error:", error);
                alert("Error: " + (error.response ? error.response.data.error : "Unknown error"));
            });
        });
    }

    // 🔹 SEARCH STUDENT FUNCTIONALITY
    let searchForm = document.getElementById("searchStudentForm");
    if (!searchForm) {
        console.error("❌ Error: #searchStudentForm not found!");
        return;
    }

    searchForm.addEventListener("submit", function (e) {
        e.preventDefault(); // ✅ Prevent page refresh

        let formData = new FormData();
        let imageInput = document.getElementById("searchImage");

        if (!imageInput.files.length) {
            alert("Please select an image to search!");
            return;
        }

        formData.append("image", imageInput.files[0]);

        console.log("🔍 Sending search request...");

        axios.post("/search", formData, {
            headers: { "Content-Type": "multipart/form-data" }
        })
        .then(response => {
            console.log("✅ Response:", response.data);

            if (response.data.error) {
                document.getElementById("result").innerHTML = `<p style="color: red;">${response.data.error}</p>`;
            } else {
                document.getElementById("result").innerHTML = `<p><strong>Name:</strong> ${response.data.name}</p>
                                                               <p><strong>ID:</strong> ${response.data.id}</p>
                                                               <p><strong>Class:</strong> ${response.data.class}</p>`;
            }
        })
        .catch(error => {
            console.error("❌ Error:", error);
            alert("Error: " + (error.response ? error.response.data.error : "Unknown error"));
        });
    });
});
