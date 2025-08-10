<script setup>
import { onMounted, ref } from 'vue'
import { fetchItems } from './api'

const items = ref([])

onMounted(async () => {
  try {
    items.value = await fetchItems()
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="container">
    <h1>Lista de Items</h1>
    <div class="item-card" v-for="item in items" :key="item.id">
      <h2>{{ item.name }}</h2>
      <p>{{ item.description }}</p>
      <small>Creado: {{ new Date(item.created_at).toLocaleString() }}</small>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.item-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 12px;
  border-radius: 8px;
  transition: transform 0.2s ease;
}

.item-card:hover {
  transform: scale(1.02);
  background-color: #f5f5f5;
}

.item-card h2 {
  margin: 0 0 5px;
  font-size: 1.2em;
}

.item-card p {
  margin: 0 0 8px;
  color: #555;
}

.item-card small {
  color: #888;
}
</style>
