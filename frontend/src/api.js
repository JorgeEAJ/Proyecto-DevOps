export async function fetchItems() {
  const response = await fetch('http://localhost:5000/api/items')
  if (!response.ok) throw new Error('Error fetching items')
  return await response.json()
}
