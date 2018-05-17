
var app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],

  data: {
    categories: [],
    products: [],
    product: null,
    category: null,
  },

  methods: {
    updateCategories() {
      fetch("/api/categories/")
        .then(response => response.json())
        .then(json => {
          this.categories = json.categories;
        });
    },

    updateProducts() {
      fetch("/api/category/" + this.category + "/")
        .then(response => response.json())
        .then(json => {
          if (!json.success) {
            console.log(json.message);
            return;
          }
          this.products = json.products;
        });
    },

    setCategory(category) {
      this.category = category;
      this.updateProducts();
    },

    setProduct(id) {
      this.issueClick(id);
      fetch("/api/product/" + id + "/")
        .then(response => response.json())
        .then(json => {
          if (!json.success) {
            console.log(json.message);
            return;
          }
          this.product = json.product;
        });
    },

    issueClick(id) {
      POST("/api/click_product/", {id: id})
        .then(response => response.json())
        .then(json => {
          if (!json.success) {
            console.log(json.message);
          }
          this.updateProducts();
        });
    },
  },

  beforeMount() {
    this.updateCategories();
  },

})

function POST(url, data) {
  return fetch(url, {
    body: JSON.stringify(data),
    method: "POST",
  })
}

