
var app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],

  data: {
    categories: [],
    products: [],
    product: null,
  },

  methods: {
    updateCategories() {
      fetch("/api/categories/")
        .then(response => response.json())
        .then(json => {
          this.categories = json.categories;
        });
    },

    setCategory(category) {
      fetch("/api/category/" + category + "/")
        .then(response => response.json())
        .then(json => {
          if (!json.success) {
            console.log(json.message);
            return;
          }
          this.products = json.products;
          this.product = null;
        });
    },

    setProduct(id) {
      fetch("/api/product/" + id + "/")
        .then(response => response.json())
        .then(json => {
          if (!json.success) {
            console.log(json.message);
            return;
          }
          this.product = json.product;
          this.issueClick(id);
        });
    },

    issueClick(id) {
      console.log("Click " + id);
    },
  },

  beforeMount() {
    this.updateCategories();
  },

})

function POST(url, data) {
  return fetch(url, {

  })
}

